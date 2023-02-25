#!/bin/bash
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
export PYTHONPATH=$SCRIPT_DIR


#python main_marl.py --config expr/leduc_poker/expr_q_learning_marl.yaml
#python main_pbt.py --config expr/leduc_poker/expr_q_learning_psro.yaml
#python main_pbt.py --config expr/kuhn_poker/expr_q_learning_psro.yaml
#python main_marl.py --config expr/kuhn_poker/expr_q_learning_marl.yaml
#python main_marl.py --config expr/gym/CartPole_DQN_marl.yaml
#python main_marl.py --config expr/gym/MountainCar_DQN_marl.yaml
#python main_marl.py --config expr/gym/Acrobot_DQN_marl.yaml

#python main_pbt.py --config expr/kuhn_poker/expr_sac_psro.yaml
#python main_marl.py --config expr/gym/CartPole_SAC_marl.yaml
#python main_marl.py --config expr/gym/Pendulum_DDPG_marl.yaml

#python main_marl.py --config expr/mpe/mpe_simple_reference_dqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_reference_madqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_reference_ppo_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_reference_mappo_marl.yaml
python main_marl.py --config expr/mpe/mpe_simple_reference_sac_marl.yaml

#python main_marl.py --config expr/mpe/mpe_simple_speaker_listener_dqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_speaker_listener_madqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_speaker_listener_ppo_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_speaker_listener_mappo_marl.yaml

#python main_marl.py --config expr/mpe/mpe_simple_spread_dqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_spread_madqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_spread_ppo_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_spread_mappo_marl.yaml

#python main_marl.py --config expr/mpe/mpe_simple_adversary_dqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_adversary_madqn_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_adversary_ppo_marl.yaml
#python main_marl.py --config expr/mpe/mpe_simple_adversary_mappo_marl.yaml

#python main_marl.py --config expr/mpe/mpe_simple_push_dqn_marl.yaml



