
# Reinforcement Learning: Theory and Python Implementation

**The First Reinforcement Learning Tutorial Book with one-on-one mapping TensorFlow 2 and PyTorch 1&2 Implementation**

| [English Edition](https://github.com/ZhiqingXiao/rl-book/tree/master/en2024) | [中文版](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2023) | [中文2019版](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2019) |
| :---: | :---: | :---: |
| [![Book](https://zhiqingxiao.github.io/rl-book/en2024/cover.jpg)](https://github.com/ZhiqingXiao/rl-book/tree/master/en2024) | [![Book](https://zhiqingxiao.github.io/rl-book/zh2023/cover.jpg)](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2023) | [![Book](https://zhiqingxiao.github.io/rl-book/zh2019/resource/cover.jpg)](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2019) |

Please email me if you are interested in publishing this book in other languages.

**Features**

This is a tutorial book on reinforcement learning, with explanation of theory and Python implementation.

- Theory: Starting from a uniform mathematical framework, this book derives the theory and algorithms of reinforcement learning, including all major algorithms such as eligibility traces and soft actor-critic algorithms.
- Practice: Every chapter is accompanied by high quality implementation based on Python 3, Gym 0.26, and TensorFlow 2 / PyTorch 1&2. All codes are compatible with Windows, Linux, and macOS, can be run in a laptop. 


### Supporting contents for English version

Check [here](https://github.com/ZhiqingXiao/rl-book/tree/master/en2024) for codes, exercise answers, etc.

### Table of Codes

All codes have been saved as a .ipynb file and a .html file in the same directory.

| Chapter | Environment & Closed-Form Policy | Agent |
| :--- | :--- | :--- |
| 2 | [CliffWalking-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/CliffWalking-v0_ClosedForm.html) | [Bellman](https://zhiqingxiao.github.io/rl-book/en2024/code/CliffWalking-v0_Bellman_demo.html) |
| 3 | [FrozenLake-v1](https://zhiqingxiao.github.io/rl-book/en2024/code/FrozenLake-v1_ClosedForm.html)| [DP](https://zhiqingxiao.github.io/rl-book/en2024/code/FrozenLake-v1_DP_demo.html) |
| 4 | [Blackjack-v1](https://zhiqingxiao.github.io/rl-book/en2024/code/Blackjack-v1_ClosedForm.html) | [MC](https://zhiqingxiao.github.io/rl-book/en2024/code/Blackjack-v1_MonteCarlo_demo.html) |
| 5 | [Taxi-v3](https://zhiqingxiao.github.io/rl-book/en2024/code/Taxi-v3_ClosedForm.html) | [SARSA](https://zhiqingxiao.github.io/rl-book/en2024/code/Taxi-v3_SARSA_demo.html), [ExpectedSARSA](https://zhiqingxiao.github.io/rl-book/en2024/code/Taxi-v3_ExpectedSARSA.html), [QL](https://zhiqingxiao.github.io/rl-book/en2024/code/Taxi-v3_QLearning.html), [DoubleQL](https://zhiqingxiao.github.io/rl-book/en2024/code/Taxi-v3_DoubleQLearning.html), [SARSA(λ)](https://zhiqingxiao.github.io/rl-book/en2024/code/Taxi-v3_SARSALambda.html) |
| 6 | [MountainCar-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_ClosedForm.html) | [SARSA](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_SARSA.html), [SARSA(λ)](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_SARSAlambda.html), DQN [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_DQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_DQN_torch.html), DoubleDQN [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_DoubleDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_DoubleDQN_torch.html), DuelDQN [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_DuelDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/MountainCar-v0_DuelDQN_torch.html) |
| 7 | [CartPole-0](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_ClosedForm.html) | VPG [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_VPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_VPG_torch.html), VPGwBaseline [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_VPGwBaseline_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_VPGwBaseline_torch.html), OffPolicyVPG [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_OffPolicyVPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_OffPolicyVPG_torch.html), OffPolicyVPGwBaseline [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_OffPolicyVPGwBaseline_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/CartPole-v0_OffPolicyVPGwBaseline_torch.html) |
| 8 | [Acrobot-v1](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_ClosedForm.html) | QAC [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_QActorCritic_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_QActorCritic_torch.html), AdvantageAC [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_AdvantageActorCritic_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_AdvantageActorCritic_torch.html), EligibilityTraceAC [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_EligibilityTraceAC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_EligibilityTraceAC_torch.html), PPO [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_PPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_PPO_torch.html), NPG [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_NPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_NPG_torch.html), TRPO [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_TRPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_TRPO_torch.html), OffPAC [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_OffPAC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Acrobot-v1_OffPAC_torch.html) |
| 9 | [Pendulum-v1](https://zhiqingxiao.github.io/rl-book/en2024/code/Pendulum-v1_ClosedForm.html) | DDPG [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Pendulum-v1_DDPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Pendulum-v1_DDPG_torch.html), TD3 [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/Pendulum-v1_TD3_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/Pendulum-v1_TD3_torch.html) |
| 10 | [LunarLander-v2](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLander-v2_ClosedForm.html) | SQL [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLander-v2_SQL_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLander-v2_SQL_torch.html), SAC [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLander-v2_SACwoA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLander-v2_SACwoA_torch.html), SACwA [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLander-v2_SACwA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLander-v2_SACwA_torch.html) |
| 10 | [LunarLanderContinuous-v2](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLanderContinuous-v2_ClosedForm.html) | SACwA [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLanderContinuous-v2_SACwA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/LunarLanderContinuous-v2_SACwA_torch.html) |
| 11 | [BipedalWalker-v3](https://zhiqingxiao.github.io/rl-book/en2024/code/BipedalWalker-v3_ClosedForm.html) | [ES](https://zhiqingxiao.github.io/rl-book/en2024/code/BipedalWalker-v3_ES.html), [ARS](https://zhiqingxiao.github.io/rl-book/en2024/code/BipedalWalker-v3_ARS.html) |
| 12 | [PongNoFrameskip-v4](https://zhiqingxiao.github.io/rl-book/en2024/code/PongNoFrameskip-v4_ClosedForm.html) | CategoricalDQN [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/PongNoFrameskip-v4_CategoricalDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/PongNoFrameskip-v4_CategoricalDQN_torch.html), QR-DQN [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/PongNoFrameskip-v4_QRDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/PongNoFrameskip-v4_QRDQN_torch.html), IQN [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/PongNoFrameskip-v4_IQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/PongNoFrameskip-v4_IQN_torch.html) |
| 13 | [BernoulliMAB-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/BernoulliMABEnv-v0_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/en2024/code/BernoulliMABEnv-v0_demo.html) |
| 13 | [GaussianMAB-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/GaussianMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/en2024/code/GaussianMABEnv_demo.html) |
| 14 | [TicTacToe-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/TicTacToe-v0_ExhaustiveSearch.html) | AlphaZero [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/TicTacToe-v0_AlphaZero_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/TicTacToe-v0_AlphaZero_torch.html)  |
| 15 | [Tiger-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/Tiger-v0_ClosedForm.html) | [VI](https://zhiqingxiao.github.io/rl-book/en2024/code/Tiger-v0_Plan_demo.html)
| 16 | [HumanoidBulletEnv-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_ClosedForm_demo.html) | BehaviorClone [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_BC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_BC_torch.html), GAIL [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_GAILPPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_GAILPPO_torch.html) |


# 强化学习：原理与Python实战

**全球第一本配套 TensorFlow 2 和 PyTorch 1/2 对照代码的强化学习教程书**

**中文版书籍支持内容**

- 代码、习题答案、勘误更新等配套资源见[这里](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2023)。

**本书内容**

- 第一部分（第 1 章）：从零开始介绍强化学习的背景知识，介绍环境库 Gym 的使用。
- 第二部分（第 2～15 章）：基于折扣奖励离散时间 Markov 决策过程模型，介绍强化学习的主干理论和常见算法。采用数学语言推导强化学习的基础理论，进而在理论的基础上讲解算法，并为算法提供配套代码实现。基础理论的讲解突出主干部分，算法讲解全面覆盖主流的强化学习算法，包括经典的非深度强化学习算法和近年流行的强化学习算法。 Python 实现和算法讲解一一对应，还给出了深度强化学习算法的 TensorFlow 和 PyTorch 对照实现。
- 第三部分（第 16 章）：介绍其他强化学习模型，包括平均奖励模型、连续时间模型、非齐次模型、半 Markov 模型、部分可观测模型等，以便更好了解强化学习研究的全貌。

**本书特色**

本书完整地介绍了主流强化学习理论。
- 选用现代强化学习理论体系，突出主干，主要定理均给出证明过程。基于理论讲解强化学习算法，全面覆盖主流强化学习算法，包括了资格迹等经典算法和 MuZero 等深度强化学习算法。
- 全书采用完整的数学体系，各章内容循序渐进。全书采用一致的数学符号，并兼容主流强化学习教程。
- 每章都配有知识点总结，并搭配习题。

本书各章均提供Python代码，实战性强。

- 简洁易懂：全书代码统一规范、简约完备，与算法讲解直接对应。
- 查阅方便：所有代码及运行结果均在 GitHub 上展示，既可以在浏览器上查阅，也可以下载到本地运行。各算法实现放在单独的文件里，可单独查阅和运行。
- 环境全面：既有 Gym 的内置环境，也有在 Gym 基础上进一步扩展的第三方环境，还带领读者一起实现自定义的环境。
- 兼容性好：所有代码在三大操作系统（Windows、macOS、Linux）上均可运行，书中给出了环境的安装和配置方法。深度强化学习代码还提供了 TensorFlow 和 PyTorch 对照代码。读者可任选其一。
- 硬件要求低：所有代码均可在没有 GPU 的个人计算机上运行。

# 强化学习：原理与Python实现 (2019)

**全球第一本配套 TensorFlow 2 代码的强化学习教程书**

**中国第一本配套 TensorFlow 2 代码的纸质算法书**

**中文版书籍支持内容**

- 代码、勘误更新等见[这里](https://github.com/ZhiqingXiao/rl-book/tree/master/zh2019)。

**本书特色**

本书介绍强化学习理论及其 Python 实现。
- 理论完备：全书用一套完整的数学体系，严谨地讲授强化学习的理论基础，主要定理均给出证明过程。各章内容循序渐进，覆盖了所有主流强化学习算法，包括资格迹等非深度强化学习算法和柔性执行者/评论者等深度强化学习算法。
- 案例丰富：在您最爱的操作系统（包括 Windows、macOS、Linux）上，基于 Python 3、Gym 0.26 和 TensorFlow 2 + PyTorch 1/2，实现强化学习算法。全书实现统一规范，体积小、重量轻。第 1～9 章给出了算法的配套实现，环境部分只依赖于 Gym 的最小安装，在没有 GPU 的计算机上也可运行；第 10～12 章介绍了多个热门综合案例，涵盖 Gym 的完整安装和自定义扩展，在有普通 GPU 的计算机上即可运行。

**QQ群**

- QQ群：722846914（勘误报错可发此群，其他问题提问前请先Google，群主和管理员不提供免费咨询服务）
- 多任务群：696984257（非小白群，多任务强化学习+强化元学习+终身强化学习+迁移强化学习，勘误报错勿发此群，提问前请先Google）
- 关于入群验证问题：由于QQ的bug，即使正确输入答案，也可能会验证失败。这时更换设备重试、更换输入法重试、改日重试均可能解决问题。如果答案中有英文字母，清注意大小写。
- 中文版书前言中给出的QQ群（935702193、243613392和948110103）已满，不再新增群成员，谢谢理解。
