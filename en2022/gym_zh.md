# Gym源码解读

| 章节 | \# | 类 | 源代码 | 解读 |
| --- | --- | --- | --- | --- |
| 1.6.2节 | Gym源码解读1-1 | 环境类`gym.Env` | [core.py](https://github.com/openai/gym/blob/master/gym/core.py) | [解读](#环境类) |
| 1.6.2节 | Gym源码解读1-2 | 空间类`gym.space.Space` | [space.py](https://github.com/openai/gym/blob/master/gym/spaces/space.py) | [解读](#空间类) |
| 1.6.2节 | Gym源码解读1-3 | 空间类`gym.space.Box` | [box.py](https://github.com/openai/gym/blob/master/gym/spaces/box.py) | [解读](#空间类Box) |
| 1.6.2节 | Gym源码解读1-4 | 空间类`gym.space.Discrete` | [discrete.py](https://github.com/openai/gym/blob/master/gym/spaces/discrete.py) | [解读](#空间类Discrete) |
| 1.6.2节 | Gym源码解读1-5 | 包装类`gym.Wrapper` | [core.py](https://github.com/openai/gym/blob/master/gym/core.py) | [解读](#包装类) |
| 1.6.2节 | Gym源码解读1-6 | 包装类`gym.wrapper.TimeLimit` | [time_limit.py](https://github.com/openai/gym/blob/master/gym/wrappers/time_limit.py) | [解读](#包装类TimeLimit) |
| 4.3.1节 | Gym源码解读4-1 | 空间类`gym.space.Tuple` | [tuple.py](https://github.com/openai/gym/blob/master/gym/spaces/tuple.py) | [解读](#空间类Tuple) |
| 11.3.1节 | Gym源码解读11-1 | 包装类`gym.wrapper.TransformReward` | [transform_reward.py](https://github.com/openai/gym/blob/master//gym/wrappers/transform_reward.py) | [解读](#包装类TransformReward) |
| 12.6.3节 | Gym源码解读12-1 | 包装类`gym.wrapper.AtariPreprocessing` | [atari_preprocessing.py](https://github.com/openai/gym/blob/master/gym/wrappers/atari_preprocessing.py) | [解读](#包装类AtariPreprocessing) |
| 12.6.3节 | Gym源码解读12-2 | 包装类`gym.wrapper.FrameStack` | [frame_stack.py](https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py) | [解读](#包装类FrameStack) |


## 环境类

环境类的成员函数：
- `reset()`：用于初始化新回合。这个成员的参数有回合使用的随机种子`seed`、提供其他初始化信息的参数`options`。返回观测`observation`和额外信息`info`。
- `step()`：用于前进一步。参数是动作`action`，返回观测`observation`、奖励信号`reward`、回合结束指示`terminated`、回合截断指示`truncated`和额外信息`info`。
- `render()`：用于绘制环境。它的参数和`metadata['render_modes']`有关。
- `close()`：用于关闭环境，释放资源。

环境类的属性：
- `action_space`：动作空间。是空间类对象。
- `observation_space`：观测空间。是空间类对象。
- `reward_range`：奖励的范围。类型为`tuple[float, float]`。
- `spec`：和任务有关的信息，比如每个回合最多有多少步等等。
- `metadata`：一些基本信息。例如，`metadata['render_modes']` 给出了支持的显示模式。类型为`dict[str, Any]`。
- `np_random`：维护随机数发生器。
- `unwrapped`：这和包装类有关。一个环境类对象可以被包装类包装起来成为一个新的环境类对象。新对象的`unwrapped`属性可以取出包装前的类的对象。

环境类的基类是`gym.Env`.


### 环境类基类`Env`

查看源码：https://github.com/openai/gym/blob/master/gym/core.py#L35


### 本书用到的环境的环境类

| 章 | 环境 | 源代码 |
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


## 空间类

空间类的作用：
- 表示观测或动作的类型。这个功能类似于Python 3的类型系统，但是它还能维护上下界等更丰富的信息。
- 随机生成空间内的样本。该功能通过成员函数`seed()`提供。实现为了实现这个功能，它维护了随机数发生器`_np_random`。成员函数`seed()`可以使用这个随机数发生器来生成随机样本。随机数发生器的构造和设置种子可参见`gym.utils.seeding`模块。

空间类的基类是`gym.spaces.Space`.

环境类中的成员`observation_space`和`action_space`需要是空间类的对象。

空间类文档（英文）：https://www.gymlibrary.dev/api/spaces/

内置的空间类：

| 空间类 | 元素类型 | 源代码 |
| --- | --- | --- |
| `Space` | 不适用 | [space.py](https://github.com/openai/gym/blob/master/gym/spaces/space.py) |
| `Box` | `np.ndarray` | [box.py](https://github.com/openai/gym/blob/master/gym/spaces/box.py) |
| `Dict` | `dict` | [dict.py](https://github.com/openai/gym/blob/master/gym/spaces/dict.py) |
| `Discrete` | `int` | [discrete.py](https://github.com/openai/gym/blob/master/gym/spaces/discrete.py) |
| `Graph` | `GraphInstance` | [graph.py](https://github.com/openai/gym/blob/master/gym/spaces/graph.py) |
| `MultiBinary` | `np.ndarray` | [multi_binary.py](https://github.com/openai/gym/blob/master/gym/spaces/multi_binary.py) |
| `MultiDiscrete` | `np.ndarray` | [multi_discrete.py](https://github.com/openai/gym/blob/master/gym/spaces/multi_discrete.py) |
| `Sequence` | `tuple` | [box.py](https://github.com/openai/gym/blob/master/gym/spaces/sequence.py) |
| `Text` | `str` | [sequence.py](https://github.com/openai/gym/blob/master/gym/spaces/text.py) |
| `Tuple` | `tuple` | [tuple.py](https://github.com/openai/gym/blob/master/gym/spaces/tuple.py) |


### 空间类基类`Space`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/space.py

抽象的空间类基类。

### 空间类`Box`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/box.py

`Box`类是最常用的空间类之一。它用来表示形如 $\mathbb{R}^n$ 、 $\mathbb{N}^n$ 、 ${[i,j]}^n$ 、 ${\lbrace i,i+1,\ldots,j\rbrace}^n$ 这样的空间，其中 $n$ 表示形状（用成员`shape`指示，可以为(3,)、(4,3)这样的）。

当某个空间为`Box`类对象时，空间上的每一个值都是`np.array`对象，并且`np.array`对象的形状就是`Box`类成员`shape`指定的形状，`np.array`的`dtype`就是`Box`类成员`dtype`指定的类型。成员`low`和`high`表示每个维度的下界和上界。`low`和`high`也可以为`-float('inf')`和`float('inf')`，表示没有上下界。

可以通过构造函数设置`shape`、`dtype`、`low`和`high`等。具体的确定空间的方法可以通过阅读源码得到。

它重载了随机抽样的成员函数`sample()`。在抽取样本时，根据每个维度是否有界，选择均匀分布、指数分布、正态分布中的一种。如果`dtype`是整数类型的，用`floor()`函数向下取整。

### 空间类`Discrete`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/discrete.py

`Discrete`类是最常用的空间类之一。它用来表示形如 $\lbrace\text{start},\ldots,\text{start}+n-1\rbrace$ 的有限集。

当空间类型为`Discrete`类时，空间内的取值为`int`型数值。

### 空间类`Tuple`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/tuple.py

当观测空间或动作空间为`gym.spaces.Tuple`类时，对应的值是`tuple`类型的。

这个类的构造函数参数`spaces`可以是`gym.space.Spaces`的列表，用来表示每个分量的空间类型。


## 包装类

包装类的作用：
- 包装类可以它把一个环境类对象包装为另外一个环境类对象，起到修改环境的效果。可能的包装包括：限制回合最大步数、限制观测值范围等等。

包装类文档（英文）：https://www.gymlibrary.dev/api/wrappers/

空间类的基类是`gym.Wrapper`.

可以用包装类的属性`unwrapped`获得包装前的环境对象。


### 包装类基类`Wrapper`

查看源码：https://github.com/openai/gym/blob/master/gym/core.py#L213

它的构造函数的参数为环境类对象`env`。

### 包装类`TimeLimit`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/time_limit.py

包装类`TimeLimit`限制每个回合的最大步数。每个回合的最大步数记录在成员`env.spec.max_episode_steps`上。当当前回合步数达到规定步数时，`step()`函数的`truncation`的返回值为`True`。

它的构造函数参数为环境类对象`env`和步数`max_episode_steps`。

### 包装类`TransformReward`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/transform_reward.py

包装类`TransformReward`的作用是把奖励用函数`f`进行变换。

它的构造函数参数为环境类对象`env`和转换函数`f`。


## Atari相关

Atari环境各版本区别可参见源代码：
https://github.com/mgbellemare/Arcade-Learning-Environment/blob/master/src/python/gym.py

### 包装类`AtariPreprocessing`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/atari_preprocessing.py

包装类`AtariPreprocessing`提供Atari游戏的常见包装。

### 包装类`FrameStack`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py

在Atari游戏中，单幅图像只能获得位置信息，而不能获得运动信息。为了捕获图像的运动信息，可以把多幅图像堆叠在一起当作状态。`FrameStack`类就实现了图像堆叠功能。对于Atari游戏，一般把4幅图像堆叠在一起。

