# Gym源码解读

| \# | 类 | 源代码 | 解读 |
| --- | --- | --- | --- |
| Gym源码解读1-1 | 环境类`gym.Env` | [源代码](https://github.com/openai/gym/blob/master/gym/core.py) | [解读](#环境类Env) |
| Gym源码解读1-2 | 空间类`gym.space.Space` | [源代码](https://github.com/openai/gym/blob/master/gym/spaces/space.py) | [解读](#空间类Space) |
| Gym源码解读1-3 | 空间类`gym.space.Box` | [源代码](https://github.com/openai/gym/blob/master/gym/spaces/box.py) | [解读](#空间类Box) |
| Gym源码解读1-4 | 空间类`gym.space.Discrete` | [源代码](https://github.com/openai/gym/blob/master/gym/spaces/discrete.py) | [解读](#空间类Discrete) |
| Gym源码解读1-5 | 包装类`gym.Wrapper` | [源代码](https://github.com/openai/gym/blob/master/gym/core.py) | [解读](#包装类Wrapper) |
| Gym源码解读1-6 | 包装类`gym.wrapper.TimeLimit` | [源代码](https://github.com/openai/gym/blob/master/gym/wrappers/time_limit.py) | [解读](#包装类TimeLimit) |
| Gym源码解读4-1 | 空间类`gym.space.Tuple` | [源代码](https://github.com/openai/gym/blob/master/gym/spaces/tuple.py) | [解读](#空间类Tuple) |
| Gym源码解读11-1 | 包装类`gym.wrapper.TransformReward` | [源代码](https://github.com/openai/gym/blob/master//gym/wrappers/transform_reward.py) | [解读](#包装类TransformReward) |
| Gym源码解读12-1 | 包装类`gym.wrapper.AtariPreprocessing` | [源代码](https://github.com/openai/gym/blob/master/gym/wrappers/atari_preprocessing.py) | [解读](#包装类AtariPreprocessing) |
| Gym源码解读12-2 | 包装类`gym.wrapper.FrameStack` | [源代码](https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py) | [解读](#包装类FrameStack) |


## 环境类`Env`

查看源码：https://github.com/openai/gym/blob/master/gym/core.py#L35

`Env`类是Gym库最重要的类之一。这个类定义了环境对象的API。我们用的所有环节对象类都是这个类的子类。

### 环境类`Env`的成员函数
- `reset()`：用于初始化新回合。这个成员的参数有回合使用的随机种子`seed`、控制本成员是否返回信息的参数`return_info`，提供其他初始化信息的参数`options`。当`return_info`为`True`时，返回观测`observation`和额外信息`info`；当`return_info`为`False`时，只返回`observation`。
- `step()`：用于前进一步。根据API版本的不同，它可能有5个或4个返回值。
- `render()`：用于绘制环境。它的参数和`metadata['render_modes']`有关。
- `close()`：用于关闭环境，释放资源。

### 环境类`Env`的属性

- `action_space`：动作空间。是`gym.spaces.Space`对象。
- `observation_space`：观测空间。是`gym.spaces.Space`对象。
- `reward_range`：奖励的范围。是两个`float`值组成的`tuple`。
- `spec`：和任务有关的信息，比如每个回合最多有多少步等等。
- `metadata`：一些基本信息。例如，`metadata['render_modes']` 给出了支持的显示模式。是一个`dict`。
- `np_random`：维护随机数发生器。
- `unwrapped`：这个是和包装类（wrapper）有关的属性。`gym.Env`类可以被包装类包装起来成为一个新的`gym.Env`子类。新类对象的`unwrapped`属性可以取出包装前的类的对象。

## 空间类`Space`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/space.py

`gym.Env`中的成员`observation_space`和`action_space`需要是空间类`gym.spaces.Space`的对象。

#### `Space`类的作用

- 表示观测或动作的类型。这个功能类似于Python 3的类型系统，但是它还能维护上下界等更丰富的信息。
- 随机生成空间内的样本。该功能通过成员函数`seed()`提供。实现为了实现这个功能，它维护了随机数发生器`_np_random`。成员函数`seed()`可以使用这个随机数发生器来生成随机样本。随机数发生器的构造和设置种子可参见`gym.utils.seeding`模块。

## 空间类`Box`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/box.py

`Box`类是最常用的`Space`类的子类之一。它用来表示形如 $\mathbb{R}^n$ 、 $\mathbb{N}^n$ 、 ${[i,j]}^n$ 、 ${\left{i,i+1,\ldots,j\right}}^n$ 这样的空间，其中 $n$ 表示形状（用成员`shape`指示，可以为(3,)、(4,3)这样的）。

当某个空间为`Box`类对象时，空间上的每一个值都是`np.array`对象，并且`np.array`对象的形状就是`Box`类成员`shape`指定的形状，`np.array`的`dtype`就是`Box`类成员`dtype`指定的类型。成员`low`和`high`表示每个维度的下界和上界。`low`和`high`也可以为`-float('inf')`和`float('inf')`，表示没有上下界。

可以通过构造函数设置`shape`、`dtype`、`low`和`high`等。具体的确定空间的方法可以通过阅读源码得到。

它重载了随机抽样的成员函数`sample()`。在抽取样本时，根据每个维度是否有界，选择均匀分布、指数分布、正态分布中的一种。如果`dtype`是整数类型的，用`floor()`函数向下取整。

## 空间类`Discrete`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/discrete.py

`Discrete`类表示空间是形如`{\text{start},\ldots\,\text{start}+n-1}`的有限集。当空间类型为`Discrete`类时，空间内的取值为`int`型数值。


## 包装类`Wrapper`

查看源码：https://github.com/openai/gym/blob/master/gym/core.py#L213

在Gym中，包装类（wrapper）可以它把一个`Env`子类包装为另外一个`Env`类的子类，起到修改环境的效果。可能的包装包括：限制回合最大步数、限制观测值范围等等。

`Wrapper`类是包装类的基类。可以通过它的属性`unwrapped`获得包装前的环境对象。`Wrapper`类构造函数的参数为环境类对象`env`，和确定成员函数`step()`返回形式的参数`new_step_api`。

## 包装类`TimeLimit`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/time_limit.py

包装类`TimeLimit`限制每个回合的最大步数。每个回合的最大步数记录在成员`env.spec.max_episode_steps`上。当当前回合步数达到规定步数时，`step()`函数的`truncation`（新API）或`done`（旧API）的返回值为`True`。这个类的成员`step()`还调用了`step_api_compatibility()`函数。这个函数能够在`new_step_api = True`时，将返回形式统一转换为新的返回形式（5个返回值）；在`new_step_api = False`时，将返回形式统一转换为旧的返回形式（4个返回值）。


## 空间类`Tuple`

查看源码：https://github.com/openai/gym/blob/master/gym/spaces/tuple.py

当观测空间或动作空间为`gym.spaces.Tuple`类时，对应的值是`tuple`类型的。

这个类的构造函数参数`spaces`可以是`gym.space.Spaces`的列表，用来表示每个分量的空间类型。


## 包装类`TransformReward`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/transform_reward.py

包装类`TransformReward`的作用是把奖励用函数`f`进行变换。


## 包装类`AtariPreprocessing`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/atari_preprocessing.py

Gym库为Atari游戏环境内置了包装类`AtariPreprocessing`，提供了Atari游戏的常见包装。


## 包装类`FrameStack`

查看源码：https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py

在电动游戏中，单幅图像只能获得位置信息，而不能获得运动信息。为了捕获图像的运动信息，可以把多幅图像堆叠在一起当作状态。`FrameStack`类就实现了图像堆叠功能。对于Atari游戏，一般把4幅图像堆叠在一起。

