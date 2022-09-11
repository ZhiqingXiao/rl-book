# Understand Gym Source Codes

- Gym GitHub repo: https://github.com/openai/gym

- Gym doc: https://www.gymlibrary.dev/

## Table of Gym Internal

| section | \# | class | codes |
| --- | --- | --- | --- |
| Section 1.6.2 | Gym Internal 1-1 | environment class `gym.Env` | [core.py](https://github.com/openai/gym/blob/master/gym/core.py) |
| Section 1.6.2 | Gym Internal 1-2 | space class `gym.space.Space` | [space.py](https://github.com/openai/gym/blob/master/gym/spaces/space.py) |
| Section 1.6.2 | Gym Internal 1-3 | space class `gym.space.Box` | [box.py](https://github.com/openai/gym/blob/master/gym/spaces/box.py) |
| Section 1.6.2 | Gym Internal 1-4 | space class `gym.space.Discrete` | [discrete.py](https://github.com/openai/gym/blob/master/gym/spaces/discrete.py) |
| Section 1.6.2 | Gym Internal 1-5 | wrapper class `gym.Wrapper` | [core.py](https://github.com/openai/gym/blob/master/gym/core.py) |
| Section 1.6.2 | Gym Internal 1-6 | wrapper class `gym.wrapper.TimeLimit` | [time_limit.py](https://github.com/openai/gym/blob/master/gym/wrappers/time_limit.py) |
| Section 4.3.1 | Gym Internal 4-1 | space class `gym.space.Tuple` | [tuple.py](https://github.com/openai/gym/blob/master/gym/spaces/tuple.py) |
| Section 11.3.1 | Gym Internal 11-1 | wrapper class `gym.wrapper.TransformReward` | [transform_reward.py](https://github.com/openai/gym/blob/master/gym/wrappers/transform_reward.py) |
| Section 12.6.3 | Gym Internal 12-1 | wrapper class `gym.wrapper.AtariPreprocessing` | [atari_preprocessing.py](https://github.com/openai/gym/blob/master/gym/wrappers/atari_preprocessing.py) |
| Section 12.6.3 | Gym Internal 12-2 | wrapper class `gym.wrapper.FrameStack` | [frame_stack.py](https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py) |

## Table of Gym Environment

| Chapter | Environment | Code |
| --- | --- | --- |
| 2 | CliffWalking | [cliffwalking.py](https://github.com/openai/gym/blob/master/gym/envs/toy_text/cliffwalking.py) |
| 3 | FrozenLake | [frozen_lake.py](https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py) |
| 4 | Blackjack | [blackjack.py](https://github.com/openai/gym/blob/master/gym/envs/toy_text/blackjack.py) |
| 5 | Taxi | [taxi.py](https://github.com/openai/gym/blob/master/gym/envs/toy_text/taxi.py) |
| 1 & 6 | MountainCar | [mountain_car.py](https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py) |
| 1 | MountainCarContinuous | [continuous_mountain_car.py](https://github.com/openai/gym/blob/master/gym/envs/classic_control/continuous_mountain_car.py) |
| 7 | CartPole | [cartpole.py](https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py) |
| 8 | Acrobot | [acrobot.py](https://github.com/openai/gym/blob/master/gym/envs/classic_control/acrobot.py) |
| 9 | Pendulum | [pendulum.py](https://github.com/openai/gym/blob/master/gym/envs/classic_control/pendulum.py) |
| 10 | LunarLander | [lunar_lander.py](https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py) |
| 10 | LunarLanderContinuous | [lunar_lander.py](https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py) |
| 11 | BipedalWalker | [bipedal_walker.py](https://github.com/openai/gym/blob/master/gym/envs/box2d/bipedal_walker.py) |

## Atari

Difference between Atari versions:
https://github.com/mgbellemare/Arcade-Learning-Environment/blob/master/src/python/gym.py