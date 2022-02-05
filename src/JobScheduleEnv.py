# coding: utf-8

import pandas as pd
import gym
import numpy as np
import datetime
import random


class JobScheduleEnv(gym.Env):
    def __init__(self, config=None):
        """ Job scheudle environment constructor

        Args:
            config: configuration of the job schedule environment
        """

        # read in configuration
        if config is None:
            self.env_config = {
                'workers': 2,
                'demands': [{'id': 0, 'start_time': 1, 'end_time': 5},
                            {'id': 1, 'start_time': 2, 'end_time': 8},
                            {'id': 2, 'start_time': 4, 'end_time': 9},
                            {'id': 3, 'start_time': 1, 'end_time': 4}]}
        else:
            self.env_config = config

        # initialization of the environment
        self._set_config()

        # initialization of the reset
        _ = self.reset()

        # set obervation and action spaces
        self.action_space = gym.spaces.Discrete(self.jobs + 1)
        self.observation_space = gym.spaces.Dict({
            'action_mask': gym.spaces.Box(0, 1, shape=(self.jobs + 1,), dtype=np.bool_),
            'job_obs': gym.spaces.Box(0.0, 1.0, shape=(self.jobs, 4), dtype=np.float),
        })

    def _set_config(self):
        """ Set environment configuration """
        self.workers = int(self.env_config['workers'])
        self.demands = self.env_config['demands']
        self.jobs = len(self.demands)

    def reset(self):
        """ Reset environment

        Returns:
            observations: observations of the environment
        """
        return self._get_obs()

    def _get_obs(self):
        """ Get observations

        Returns:
            observations: observations of the environment
        """

        return self.observation_space

    def _get_actions(self):
        """ Get actions

        Returns:
            actions: actions to take at the moment
        """
        return self.action_space

    @property
    def observation_space(self):
        """ Observation space """
        return self._get_obs()

    @property
    def action_space(self):
        """ Action space """
        return self._get_actions()