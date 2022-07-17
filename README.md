
# Reinforcement Learning: Theory and Python Implementation

**The First Reinforcement Learning Tutorial Book with one-on-one mapping TensorFlow 2 and PyTorch 1 Implementation**

| [English Edition](https://github.com/ZhiqingXiao/rl-book/tree/master/en2022) | [中文版](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2019) |
| :---: | :---: |
| ![Book](https://zhiqingxiao.github.io/rl-book/en2022/cover.jpg)| ![Book](https://zhiqingxiao.github.io/rl-book/zh2019/resource/cover.jpg) |

Please email me if you are interested in publishing this book in other languages.

**Features**

This is a tutorial book on reinforcement learning, with explanation of theory and Python implementation.

- Theory: Starting from a uniform mathematical framework, this book derives the theory and algorithms of reinforcement learning, including all major algorithms such as eligibility traces and soft actor-critic algorithms.
- Practice: Every chapter is accompanied by high quality implementation based on Python 3.10, Gym 0.24, and TensorFlow 2 / PyTorch 1. All codes are compatible with Windows, Linux, and macOS, can be run in a laptop. 


### Supporting contents for English version

Check [here](https://github.com/ZhiqingXiao/rl-book/tree/master/en2022) for codes, exercise answers, etc.

### Table of Codes

All codes have been saved as a .ipynb file in the directory "ipynb" and a .html file in the directory "html".

| Chapter | Environment & Closed-Form Policy | Agent |
| :--- | :--- | :--- |
| 2 | [CliffWalking-v0](https://zhiqingxiao.github.io/rl-book/html/CliffWalking-v0_ClosedForm.html) | [Bellman](https://zhiqingxiao.github.io/rl-book/html/CliffWalking-v0_Bellman_demo.html) |
| 3 | [FrozenLake-v1](https://zhiqingxiao.github.io/rl-book/html/FrozenLake-v1_ClosedForm.html)| [DP](https://zhiqingxiao.github.io/rl-book/html/FrozenLake-v1_DP_demo.html) |
| 4 | [Blackjack-v1](https://zhiqingxiao.github.io/rl-book/html/Blackjack-v1_ClosedForm.html) | [MC](https://zhiqingxiao.github.io/rl-book/html/Blackjack-v1_MonteCarlo_demo.html) |
| 5 | [Taxi-v3](https://zhiqingxiao.github.io/rl-book/html/Taxi-v3_ClosedForm.html) | [SARSA](https://zhiqingxiao.github.io/rl-book/html/Taxi-v3_SARSA_demo.html), [ExpectedSARSA](https://zhiqingxiao.github.io/rl-book/html/Taxi-v3_ExpectedSARSA.html), [QL](https://zhiqingxiao.github.io/rl-book/html/Taxi-v3_QLearning.html), [DoubleQL](https://zhiqingxiao.github.io/rl-book/html/Taxi-v3_DoubleQLearning.html), [SARSA(λ)](https://zhiqingxiao.github.io/rl-book/html/Taxi-v3_SARSALambda.html) |
| 6 | [MountainCar-v0](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_ClosedForm.html) | [SARSA](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_SARSA.html), [SARSA(λ)](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_SARSAlambda.html), DQN [tf](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_DQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_DQN_torch.html), DoubleDQN [tf](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_DoubleDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_DoubleDQN_torch.html), DuelDQN [tf](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_DuelDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/MountainCar-v0_DuelDQN_torch.html) |
| 7 | [CartPole-0](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_ClosedForm.html) | VPG [tf](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_VPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_VPG_torch.html), VPGwBaseline [tf](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_VPGwBaseline_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_VPGwBaseline_torch.html), OffPolicyVPG [tf](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_OffPolicyVPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_OffPolicyVPG_torch.html), OffPolicyVPGwBaseline [tf](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_OffPolicyVPGwBaseline_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/CartPole-v0_OffPolicyVPGwBaseline_torch.html) |
| 8 | [Acrobot-v1](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_ClosedForm.html) | QAC [tf](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_QActorCritic_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_QActorCritic_torch.html), AdvantageAC [tf](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_AdvantageActorCritic_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_AdvantageActorCritic_torch.html), EligibilityTraceAC [tf](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_EligibilityTraceAC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_EligibilityTraceAC_torch.html), PPO [tf](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_PPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_PPO_torch.html), NPG [tf](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_NPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_NPG_torch.html), TRPO [tf](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_TRPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_TRPO_torch.html), OffPAC [tf](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_OffPAC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Acrobot-v1_OffPAC_torch.html) |
| 9 | [Pendulum-v1](https://zhiqingxiao.github.io/rl-book/html/Pendulum-v1_ClosedForm.html) | DDPG [tf](https://zhiqingxiao.github.io/rl-book/html/Pendulum-v1_DDPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Pendulum-v1_DDPG_torch.html), TD3 [tf](https://zhiqingxiao.github.io/rl-book/html/Pendulum-v1_TD3_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/Pendulum-v1_TD3_torch.html) |
| 10 | [LunarLander-v2](https://zhiqingxiao.github.io/rl-book/html/LunarLander-v2_ClosedForm.html) | SQL [tf](https://zhiqingxiao.github.io/rl-book/html/LunarLander-v2_SQL_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/LunarLander-v2_SQL_torch.html), SAC [tf](https://zhiqingxiao.github.io/rl-book/html/LunarLander-v2_SACwoA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/LunarLander-v2_SACwoA_torch.html), SACwA [tf](https://zhiqingxiao.github.io/rl-book/html/LunarLander-v2_SACwA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/LunarLander-v2_SACwA_torch.html) |
| 10 | [LunarLanderContinuous-v2](https://zhiqingxiao.github.io/rl-book/html/LunarLanderContinuous-v2_ClosedForm.html) | SACwA [tf](https://zhiqingxiao.github.io/rl-book/html/LunarLanderContinuous-v2_SACwA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/LunarLanderContinuous-v2_SACwA_torch.html) |
| 11 | [BipedalWalker-v3](https://zhiqingxiao.github.io/rl-book/html/BipedalWalker-v3_ClosedForm.html) | [ES](https://zhiqingxiao.github.io/rl-book/html/BipedalWalker-v3_ES.html), [ARS](https://zhiqingxiao.github.io/rl-book/html/BipedalWalker-v3_ARS.html) |
| 12 note1 | [PongNoFrameskip-v4](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_ClosedForm.html) | CategoricalDQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_CategoricalDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_CategoricalDQN_torch.html), QR-DQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_QRDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_QRDQN_torch.html), IQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_IQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_IQN_torch.html) |
| 13 | [BernoulliMAB-v0](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) |
| 13 | [GaussianMAB-v0](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/html/GaussianMABEnv_demo.html) |
| 14 | [TicTacToe-v0](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_ExhaustiveSearch.html) | AlphaZero [tf](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_AlphaZero_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_AlphaZero_torch.html)  |
| 15 note2 | [HumanoidBulletEnv-v0](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_ClosedForm_demo.html) | BehaviorClone [tf](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_BC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_BC_torch.html), GAIL [tf](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_GAILPPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_GAILPPO_torch.html) |
| 16 | [Tiger-v0](https://zhiqingxiao.github.io/rl-book/html/Tiger-v0_ClosedForm.html) | [VI](https://zhiqingxiao.github.io/rl-book/html/Tiger-v0_Plan_demo.html)


Notes:
1. It does not work with Gym 0.25. It is because the `wrapper.FrameStack` class in Gym 0.25 is buggy.
2. It does not work with Gym 0.25 and PyBullet 3.2.4. It is because Gym 0.25 changed `metadata["render.modes"]` to `metadata["render_modes"]`, but PyBullet releases have not updated accordingly yet.


# 强化学习：原理与Python实现

**全球第一本配套 TensorFlow 2 代码的强化学习教程书**

**中国第一本配套 TensorFlow 2 代码的纸质算法书**

**现已提供 TensorFlow 2 和 PyTorch 1 [对照代码](https://zhiqingxiao.github.io/rl-book/#table-of-codes)**


**中文版书籍支持内容**

- 代码、勘误更新等见[这里](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2019)。

**本书特色**

本书介绍强化学习理论及其 Python 实现。
- 理论完备：全书用一套完整的数学体系，严谨地讲授强化学习的理论基础，主要定理均给出证明过程。各章内容循序渐进，覆盖了所有主流强化学习算法，包括资格迹等非深度强化学习算法和柔性执行者/评论者等深度强化学习算法。
- 案例丰富：在您最爱的操作系统（包括 Windows、macOS、Linux）上，基于 Python 3.10、Gym 0.24 和 TensorFlow 2 / PyTorch 1，实现强化学习算法。全书实现统一规范，体积小、重量轻。第 1～9 章给出了算法的配套实现，环境部分只依赖于 Gym 的最小安装，在没有 GPU 的计算机上也可运行；第 10～12 章介绍了多个热门综合案例，涵盖 Gym 的完整安装和自定义扩展，在有普通 GPU 的计算机上即可运行。

**TensorFlow 2 和 PyTorch 1 对照代码**

- 本书深度强化学习部分新增基于 TensorFlow 2 和 PyTorch 1 的 [对照实现](https://zhiqingxiao.github.io/rl-book/#table-of-codes)。两个版本实现均和正文伪代码严格对应，两个版本仅在智能体部分实现不同，程序结构和智能体参数完全相同。ipynb格式见notebooks文件夹，HTML网页格式见html文件夹，两个版本内容相同。

- 代码已经过Python 3.10、Gym 0.24、TensorFlow 2和PyTorch 1验证。有错误请报错。

**QQ群**

- QQ群：722846914（勘误报错可发此群，其他问题提问前请先Google，群主和管理员不提供免费咨询服务）
- 多任务群：696984257（非小白群，多任务强化学习+强化元学习+终身强化学习+迁移强化学习，勘误报错勿发此群，提问前请先Google）
- 关于入群验证问题：由于QQ的bug，即使正确输入答案，也可能会验证失败。这时更换设备重试、更换输入法重试、改日重试均可能解决问题。如果答案中有英文字母，清注意大小写。
- 中文版书前言中给出的QQ群（935702193、243613392和948110103）已满，不再新增群成员，谢谢理解。
