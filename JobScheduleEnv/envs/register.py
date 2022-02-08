import gym

gym.envs.register(
     id='jse-v0',
     entry_point='JobScheduleEnv:JobScheduleEnv',
     max_episode_steps=1000,
     kwargs={'config' : None},
)