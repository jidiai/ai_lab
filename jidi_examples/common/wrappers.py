# -*- coding:utf-8  -*-
# Time  : 2021/02/26 16:18
# Author: Yutong Wu

import numpy as np

class classic_CartPole_v0_wrapper(object):
    def __init__(self, env):
        self.env = env

    def action_space(self):
        return self.env.action_dim

    def state_space(self):
        return self.env.input_dimension.shape[0]

    def action(self, a):
        print('a', a)
        a = [a]
        joint_action_ = []
        for n in range(self.env.n_player):
            action_a = a[n]
            each = [0] * self.env.action_dim
            each[action_a] = 1
            action_one_hot = [[each]]
            joint_action_.append([action_one_hot[0][0]])
        return joint_action_

    def reward(self, r):
        return np.array(r)

    def observation(self, o):
        # todo: classical env reset产生的observation和env.step的不同
        state = np.array(o)
        return state
