# Understand Gym Source Codes

- Gym GitHub repo: https://github.com/openai/gym
- Gym doc: https://www.gymlibrary.dev


## Table of Gym Internal

| section | class | codes | note |
| --- | --- | --- | --- | --- |
| Section 1.6.2 | environment class `gym.Env` | [core.py](https://github.com/openai/gym/blob/master/gym/core.py) | [Note](#environment-classes) |
| Section 1.6.2 | space class `gym.space.Space` | [space.py](https://github.com/openai/gym/blob/master/gym/spaces/space.py) | [Note](#space-classes) |
| Section 1.6.2 | space class `gym.space.Box` | [box.py](https://github.com/openai/gym/blob/master/gym/spaces/box.py) | [Note](#the-class-box) |
| Section 1.6.2 | space class `gym.space.Discrete` | [discrete.py](https://github.com/openai/gym/blob/master/gym/spaces/discrete.py) | [Note](#the-class-discrete) |
| Section 1.6.2 | wrapper class `gym.Wrapper` | [core.py](https://github.com/openai/gym/blob/master/gym/core.py) | [Note](#wrapper-classes) |
| Section 1.6.2 | wrapper class `gym.wrapper.TimeLimit` | [time_limit.py](https://github.com/openai/gym/blob/master/gym/wrappers/time_limit.py) | [Note](#the-class-timelimit) |
| Section 4.3.1 | space class `gym.space.Tuple` | [tuple.py](https://github.com/openai/gym/blob/master/gym/spaces/tuple.py) | [Note](#the-class-tuple) |
| Section 11.3.1 | wrapper class `gym.wrapper.TransformReward` | [transform_reward.py](https://github.com/openai/gym/blob/master/gym/wrappers/transform_reward.py) | [Note](#the-class-transformreward) |
| Section 12.6.3 | wrapper class `gym.wrapper.AtariPreprocessing` | [atari_preprocessing.py](https://github.com/openai/gym/blob/master/gym/wrappers/atari_preprocessing.py) | [Note](#the-class-ataripreprocessing) |
| Section 12.6.3 | wrapper class `gym.wrapper.FrameStack` | [frame_stack.py](https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py) | [Note](#the-class-framestack) |


## Environment Classes

The member functions of an environment class:
- `reset()`: used for initializing a new episode. Its parameters include the seed of random number generator `seed` and `options` for other configurations. It returns `observation` and extra information `info`.
- `step()`: one interaction step. Its paramter is the action `action`. It returns next observation `observation`, the reward signal `reward`, the indicator of episode termination `terminated`, the indicator of episode truncation `truncated`, and extra information `info`.
- `render()`: visualize the environment. The visualization method is specified in the attribute `render_mode`.
- `close()`: close the environment and release resources.

The member variables and attributes of an environment class:
- `observation_space`: the observation space. It’s an object of a space class.
- `action_space`: the action space. It’s an object of a space class.
- `reward_range`: the range of rewards. Its type is `tuple[float, float]`.
- `spec`: specification of the task, such as what is the maximum number of steps in an episode.
- `metadata`: some basic information. For example, `metadata['render_modes']` shows what render modes are supported. It is a dict.
- `render_mode`: the visualization way. Its value should be within `metadata['render_modes']`.
- `np_random`: Random number generator.
- `unwrapped`: This property relates wrapper classes. An environment object can be wrapped to a new environment object. We can access the instance of the object before wrapped using the property `unwrapped` of the instance of the new object.


### The class `Env`

The class `Env` is the base class of all envionment classes.

Source Codes: https://github.com/openai/gym/blob/master/gym/core.py#L35

### Table of Gym Environments in the book

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

## Space Classes

Funtionarlities of space classes:
- Represent the type of observation or action. It is alike the typing system in Python 3, but it can also maintain more information such as lower bound and upper bound.
- Generate random samples. This function is provided the member function `seed()`. The class also maintains a random number generator `_np_random` for this function. The member function `seed()` can use this random number generator to generate random samples. The details of construction and seeding can be found in the module `gym.utils.seeding`.

The member of an environment class `observation_space` and `action_space` should be instances of space classes.

Documents for space classes: https://www.gymlibrary.dev/api/spaces/

Table of built-in space classes

| Space Class | Type of Elements | Source Codes |
| --- | --- | --- |
| `Space` | N/A | [space.py](https://github.com/openai/gym/blob/master/gym/spaces/space.py) |
| `Box` | `np.ndarray` | [box.py](https://github.com/openai/gym/blob/master/gym/spaces/box.py) |
| `Dict` | `dict` | [dict.py](https://github.com/openai/gym/blob/master/gym/spaces/dict.py) |
| `Discrete` | `int` | [discrete.py](https://github.com/openai/gym/blob/master/gym/spaces/discrete.py) |
| `Graph` | `GraphInstance` | [graph.py](https://github.com/openai/gym/blob/master/gym/spaces/graph.py) |
| `MultiBinary` | `np.ndarray` | [multi_binary.py](https://github.com/openai/gym/blob/master/gym/spaces/multi_binary.py) |
| `MultiDiscrete` | `np.ndarray` | [multi_discrete.py](https://github.com/openai/gym/blob/master/gym/spaces/multi_discrete.py) |
| `Sequence` | `tuple` | [box.py](https://github.com/openai/gym/blob/master/gym/spaces/sequence.py) |
| `Text` | `str` | [sequence.py](https://github.com/openai/gym/blob/master/gym/spaces/text.py) |
| `Tuple` | `tuple` | [tuple.py](https://github.com/openai/gym/blob/master/gym/spaces/tuple.py) |


### The class `Space`

The class `Space` is the base class of all space classes.

Source Codes: https://github.com/openai/gym/blob/master/gym/spaces/space.py


### The class `Box`

Source codes: https://github.com/openai/gym/blob/master/gym/spaces/box.py


The class `Box` is one of the most frequently used subclasses of the class Space. It represents the space in the form of $\mathbb{R}^n$, $\mathbb{N}^n$, ${[i,j]}^n$, ${\lbrace i,i+1,\ldots,j\rbrace}^n$, where $n$ is the shape. The shape is indicated by the member shape, and its value can be (3,), (4,3), and so on.

If a space is a `Box` object, the value is a `np.array` object. The shape of the `np.array` is exactly the member `shape` of the `Box` object, and the `dtype` of `np.array` is exactly the member `dtype` of the `Box` object. The member `low` and the member `high` indicate the lower bound and the upper bound on values respectively. low and high can be `-float('inf')` and `float('inf')` respectively, meaning that there are no bounds.

We can set its `shape`, `dtype`, `low`, and `high` via its constructor. Details can be inferred from the source codes.

It overrides the member function `sample()`. Then generating random samples, it picks one of distribution among uniform distribution, exponential distribution, and Gaussian distribution, according to whether the component is bounded. If the `dtype` is an integral type, it applies the `floor()` function to ensure that the values are integers.

### The class `Discrete`

Source codes: https://github.com/openai/gym/blob/master/gym/spaces/discrete.py


The class `Discrete` is one of the most frequently used space classes. It represents a finite set in the form of $\lbrace\text{start},\ldots,\text{start}+n-1\rbrace$. A value of a `Discrete` space is an `int`.

### The class `Tuple`

The space class `gym.spaces.Tuple` maps the the value type `tuple`.

The constructor of this class accepts the parameters `spaces`, which can be a `list` of space class objects that designate space for each element.


## Wrapper Classes

Wrapper classes wrap a environment class instance to another environment class instance, so that it modifies the old environment. Possible impacts of wrapping include: limit the step number in an episode, or limit the range of observations.

We can access the object before wrapped via its property `unwrapped`.

Documents for wrapper classes: https://www.gymlibrary.dev/api/wrappers/

### The class `Wrapper`

The class `Wrapper` is the base class of all wrapper classes.

Source Codes: https://github.com/openai/gym/blob/master/gym/core.py#L213
The parameters of its constructor is the environment object `env`.

### The class `TimeLimit`

Source codes: https://github.com/openai/gym/blob/master/gym/wrappers/time_limit.py

The wrapper class `TimeLimit` limits the maximum number of steps in each episode. When the step number of the current episode reaches the designated value, the function `step()` returns `truncated` as `True`.

The parameters of its contructor are the environment class instance `env` and the step number `max_episode_steps`.

For environments that have been registered in Gym, the maximum number of steps in an episode is recorded in `env.spec.max_episode_steps`.

### The class `TransformReward`

Source codes: https://github.com/openai/gym/blob/master/gym/wrappers/transform_reward.py

The class `TransformReward` transforms rewards using a function `f`.

The parameters of its constructor are the envionment object `env` and the function `f`.


## Atari

Difference between Atari versions:
https://github.com/mgbellemare/Arcade-Learning-Environment/blob/master/src/python/gym.py

### The class `AtariPreprocessing`

Source codes: https://github.com/openai/gym/blob/master/gym/wrappers/atari_preprocessing.py

The wrapper class `AtariPreprocessing` provides common wrapper for Atari games.

### The class `FrameStack`

Source codes: https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py

In Atari environments, a single image of a video game can only show the position of objects, but can not show the movement of the objects. In order to obtain the movement information, we can stack multiple images together as the state. The class FrameStack implements the stack. Atari games usually stack 4 images.
