from typing import OrderedDict
from registry import registry
from agent.agent_manager import AgentManager

from agent.policy_data.policy_data_manager import PolicyDataManager
from utils.logger import Logger
from agent import Population
from utils.desc.task_desc import TrainingDesc
import numpy as np
import importlib

from collections import OrderedDict

class MARLScheduler:
    def __init__(self,cfg,agent_manager:AgentManager,population_id:str,policy_data_manager:PolicyDataManager):
        self.cfg=cfg
        self.agent_manager=agent_manager
        self.agents=self.agent_manager.agents
        self.population_id=population_id
        self.policy_data_manager=policy_data_manager
        self.meta_solver_type=self.cfg.get("meta_solver","nash")
        self.sync_training=self.cfg.get("sync_training",False)

        Logger.warning("use meta solver type: {}".format(self.meta_solver_type))
        solver_module=importlib.import_module("light_malib.framework.meta_solver.{}".format(self.meta_solver_type))
        self.meta_solver=solver_module.Solver()
        self._schedule=self._gen_schedule()

    def _gen_schedule(self):

        for training_agent_id in self.agents.training_agent_ids:
            agent_id2policy_ids = OrderedDict()
            agent_id2policy_indices = OrderedDict()
            for agent_id in self.agents.keys():
                population: Population = self.agents[agent_id].populations[self.population_id]
                agent_id2policy_ids[agent_id] = population.policy_ids
                agent_id2policy_indices[agent_id] = np.array(
                    [self.agents[agent_id].policy_id2idx[policy_id] for policy_id in population.policy_ids])



            policy_distributions = {}
            agent_0_dist = zip(['agent_0_default_0'], [1])
            agent_1_dist = zip(['q1', 'q2', 'q3'], [1/3,1/3,1/3])
            policy_distributions['agent_0'] = OrderedDict(agent_0_dist)
            policy_distributions['agent_1'] = OrderedDict(agent_1_dist)

            stopper = registry.get(registry.STOPPER, self.cfg.stopper.type)(policy_data_manager=self.policy_data_manager,
                                                                            **self.cfg.stopper.kwargs)

            training_policy_id = 'agent_0_default_0'

            training_desc = TrainingDesc(
                training_agent_id,
                training_policy_id,
                policy_distributions,
                self.agents.share_policies,
                self.sync_training,
                stopper
            )
            yield training_desc

    def get_task(self):
        try:
            task = next(self._schedule)
            return task
        except StopIteration:
            return None

    def submit_result(self, result):
        pass
