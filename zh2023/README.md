# 强化学习：原理与Python实战

**全球首本配套 TensorFlow 2 和 PyTorch 1/2 对照代码的强化学习教程书**

**剖析 ChatGPT 关键技术 PPO 和 RLHF**

![Book](https://zhiqingxiao.github.io/images/book/rlzh2023.jpg)

**配套资源**

- 习题参考答案：[链接](https://zhiqingxiao.github.io/rl-book/zh2023/choice.html)
- 开发环境搭建：[Windows](https://github.com/ZhiqingXiao/rl-book/blob/master/zh2023/setup/setupwin.md) [macOS](https://github.com/ZhiqingXiao/rl-book/blob/master/zh2023/setup/setupmac.md)
- 数学字母表：[链接](https://github.com/ZhiqingXiao/rl-book/blob/master/zh2023/notation.md)
- 缩略语表：[链接](https://github.com/zhiqingxiao/rl-book/blob/master/zh2023/abbreviation.md)
- Gym源码解读：[链接](https://github.com/ZhiqingXiao/rl-book/blob/master/zh2023/gym.md)
- 参考文献：[链接](https://github.com/zhiqingxiao/rl-book/blob/master/zh2023/bibliography.md)
- 勘误更新：[链接](https://github.com/zhiqingxiao/rl-book/blob/master/zh2023/errata.md)

**代码**

列表索引：[链接](https://github.com/zhiqingxiao/rl-book/blob/master/zh2023/code.md)

| 章 | 环境和闭式解 | 智能体 |
| :--- | :--- | :--- |
| 2 | [CliffWalking-v0](https://zhiqingxiao.github.io/rl-book/en2023/code/CliffWalking-v0_ClosedForm.html) | [Bellman](https://zhiqingxiao.github.io/rl-book/en2023/code/CliffWalking-v0_Bellman_demo.html) |
| 3 | [FrozenLake-v1](https://zhiqingxiao.github.io/rl-book/en2023/code/FrozenLake-v1_ClosedForm.html)| [DP](https://zhiqingxiao.github.io/rl-book/en2023/code/FrozenLake-v1_DP_demo.html) |
| 4 | [Blackjack-v1](https://zhiqingxiao.github.io/rl-book/en2023/code/Blackjack-v1_ClosedForm.html) | [MC](https://zhiqingxiao.github.io/rl-book/en2023/code/Blackjack-v1_MonteCarlo_demo.html) |
| 5 | [Taxi-v3](https://zhiqingxiao.github.io/rl-book/en2023/code/Taxi-v3_ClosedForm.html) | [SARSA](https://zhiqingxiao.github.io/rl-book/en2023/code/Taxi-v3_SARSA_demo.html), [ExpectedSARSA](https://zhiqingxiao.github.io/rl-book/en2023/code/Taxi-v3_ExpectedSARSA.html), [QL](https://zhiqingxiao.github.io/rl-book/en2023/code/Taxi-v3_QLearning.html), [DoubleQL](https://zhiqingxiao.github.io/rl-book/en2023/code/Taxi-v3_DoubleQLearning.html), [SARSA(λ)](https://zhiqingxiao.github.io/rl-book/en2023/code/Taxi-v3_SARSALambda.html) |
| 6 | [MountainCar-v0](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_ClosedForm.html) | [SARSA](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_SARSA.html), [SARSA(λ)](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_SARSAlambda.html), DQN [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_DQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_DQN_torch.html), DoubleDQN [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_DoubleDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_DoubleDQN_torch.html), DuelDQN [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_DuelDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/MountainCar-v0_DuelDQN_torch.html) |
| 7 | [CartPole-0](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_ClosedForm.html) | VPG [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_VPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_VPG_torch.html), VPGwBaseline [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_VPGwBaseline_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_VPGwBaseline_torch.html), OffPolicyVPG [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_OffPolicyVPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_OffPolicyVPG_torch.html), OffPolicyVPGwBaseline [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_OffPolicyVPGwBaseline_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/CartPole-v0_OffPolicyVPGwBaseline_torch.html) |
| 8 | [Acrobot-v1](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_ClosedForm.html) | QAC [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_QActorCritic_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_QActorCritic_torch.html), AdvantageAC [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_AdvantageActorCritic_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_AdvantageActorCritic_torch.html), EligibilityTraceAC [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_EligibilityTraceAC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_EligibilityTraceAC_torch.html), PPO [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_PPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_PPO_torch.html), NPG [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_NPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_NPG_torch.html), TRPO [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_TRPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_TRPO_torch.html), OffPAC [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_OffPAC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Acrobot-v1_OffPAC_torch.html) |
| 9 | [Pendulum-v1](https://zhiqingxiao.github.io/rl-book/en2023/code/Pendulum-v1_ClosedForm.html) | DDPG [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Pendulum-v1_DDPG_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Pendulum-v1_DDPG_torch.html), TD3 [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/Pendulum-v1_TD3_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/Pendulum-v1_TD3_torch.html) |
| 10 | [LunarLander-v2](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLander-v2_ClosedForm.html) | SQL [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLander-v2_SQL_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLander-v2_SQL_torch.html), SAC [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLander-v2_SACwoA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLander-v2_SACwoA_torch.html), SACwA [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLander-v2_SACwA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLander-v2_SACwA_torch.html) |
| 10 | [LunarLanderContinuous-v2](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLanderContinuous-v2_ClosedForm.html) | SACwA [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLanderContinuous-v2_SACwA_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/LunarLanderContinuous-v2_SACwA_torch.html) |
| 11 | [BipedalWalker-v3](https://zhiqingxiao.github.io/rl-book/en2023/code/BipedalWalker-v3_ClosedForm.html) | [ES](https://zhiqingxiao.github.io/rl-book/en2023/code/BipedalWalker-v3_ES.html), [ARS](https://zhiqingxiao.github.io/rl-book/en2023/code/BipedalWalker-v3_ARS.html) |
| 12 | [PongNoFrameskip-v4](https://zhiqingxiao.github.io/rl-book/en2023/code/PongNoFrameskip-v4_ClosedForm.html) | CategoricalDQN [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/PongNoFrameskip-v4_CategoricalDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/PongNoFrameskip-v4_CategoricalDQN_torch.html), QR-DQN [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/PongNoFrameskip-v4_QRDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/PongNoFrameskip-v4_QRDQN_torch.html), IQN [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/PongNoFrameskip-v4_IQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/PongNoFrameskip-v4_IQN_torch.html) |
| 13 | [BernoulliMAB-v0](https://zhiqingxiao.github.io/rl-book/en2023/code/BernoulliMABEnv-v0_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/en2023/code/BernoulliMABEnv-v0_demo.html) |
| 13 | [GaussianMAB-v0](https://zhiqingxiao.github.io/rl-book/en2023/code/GaussianMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/en2023/code/GaussianMABEnv_demo.html) |
| 14 | [TicTacToe-v0](https://zhiqingxiao.github.io/rl-book/en2023/code/TicTacToe-v0_ExhaustiveSearch.html) | AlphaZero [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/TicTacToe-v0_AlphaZero_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/TicTacToe-v0_AlphaZero_torch.html)  |
| 15 注 | [HumanoidBulletEnv-v0](https://zhiqingxiao.github.io/rl-book/en2023/code/HumanoidBulletEnv-v0_ClosedForm_demo.html) | BehaviorClone [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/HumanoidBulletEnv-v0_BC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/HumanoidBulletEnv-v0_BC_torch.html), GAIL [tf](https://zhiqingxiao.github.io/rl-book/en2023/code/HumanoidBulletEnv-v0_GAILPPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2023/code/HumanoidBulletEnv-v0_GAILPPO_torch.html) |
| 16 | [Tiger-v0](https://zhiqingxiao.github.io/rl-book/en2023/code/Tiger-v0_ClosedForm.html) | [VI](https://zhiqingxiao.github.io/rl-book/en2023/code/Tiger-v0_Plan_demo.html)


注:
1. 此案例在 Gym >=0.25 且 PyBullet 3.2.4 的环境中无法工作。原因：Gym 0.25 把 `metadata["render.modes"]` 改成了 `metadata["render_modes"]`, 但是 PyBullet 未更新发行版。


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

**QQ群**

- QQ群：722846914（勘误报错可发此群，其他问题提问前请先Google，群主和管理员不提供免费咨询服务）
- 多任务群：696984257（非小白群，多任务强化学习+强化元学习+终身强化学习+迁移强化学习，勘误报错勿发此群，提问前请先Google）
- 关于入群验证问题：由于QQ的bug，即使正确输入答案，也可能会验证失败。这时更换设备重试、更换输入法重试、改日重试均可能解决问题。如果答案中有英文字母，请注意大小写。

**热心读者 [Anesck](https://github.com/anesck) 对本书知识点的梳理评注**

[第1章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/1.chapter_one.html) 
[第2章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/2.chapter_two.html) 
[第3章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/3.chapter_three.html) 
[第4章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/4.chapter_four.html) 
[第5章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/5.chapter_five.html) 
[第6章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/6.chapter_six.html) 
[第7章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/7.chapter_seven.html) 
[第8章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/8.chapter_eight.html) 
[第9章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/9.chapter_nine.html) 

**常见问题**

- 问：Windows系统下安装TensorFlow或PyTorch失败。答：请在Windows 10/11里安装Visual Studio 2022（如果有旧版本的Visual Studio请先彻底卸载）。更多细节和安装问题请自行Google。PyTorch安装可参阅：https://mp.weixin.qq.com/s/uRx1XOPrfFOdMlRU6I-eyA

- 问：在Visual Studio或Visual Studio Code或PyCharm里面运行代码失败，比如找不到函数`display()`。答：本repo代码是配套Jupyter Notebook环境的，只能在Jupyter Notebook里运行。推荐您安装最新版本的Anaconda并直接运行下载来的Notebook。（`display()`函数是Jupyter Notebook里才有的函数。）不需要安装Visual Studio Code或PyCharm。更多细节或其他错误请自行Google。

- 问：GPU会比CPU跑的快么？答：没有用到TensorFlow和PyTorch的代码，不会用到GPU。用到TensorFlow和PyTorch的代码，由于网络一般不大，GPU反而可能更慢。PyTorch代码使用GPU时要把Tensor对象放在GPU上（可能需要修改代码）。

# Reinforcement Learning: Theory and Python Implementation (Chinese 2023 edition)

**The First Reinforcement Learning Tutorial Book with one-on-one mapping TensorFlow 2 and PyTorch 1/2 Implementation**

**Features**

This book comprehensively introduces the mainstream RL theory.

- This book introduces the trunk of the modern RL theory in a systematically way. All major results are accompanied with proofs. We introduce the algorithms based on the theory, which covers all mainstream RL algorithms, including both classical RL algorithms such as eligibility trace and deep RL algorithm such as MuZero.
- This book uses a consistent set of mathematical notations, which are compatible with mainstream RL tutorials.

All chapters are accompanied with Python codes.

- Easy to understand: All codes are implemented in a consistent and concise way, which directly maps to the explanation of algorithms.
- Easy to check: All codes and running results are shown in GitHub. We can either browse them in the web browser, or download locally to run them. Every algorithm is implemented in a self-contained standalone file, which can be browsed and executed individually.
- Diverse environments: We not only consider the built-in tasks in the library Gym, but also consider the third-party extension of the Gym. We even create environments for our own tasks.
- Highly compatible: All codes can be run in any one of all three major operating systems (Windows, macOS, and Linux). The methods to setup the environments are provided. Deep RL algorithms are implemented based on both TensorFlow 2 and PyTorch 1&2, so that readers can choose any one among the two or have a one-to-one comparison.
- Based on latest versions of software: All codes are based on the latest version of Python and its extension packages. The codes in GitHub will be updated according to the software update.
- Little hardware requirement: All codes can be run in a PC without GPU.

**Table of Contents**

01. Introduction of Reinforcement Learning
02. Markov Decision Process
03. Model-based Numeric Iteration
04. MC: Monte-Carlo Learning
05. TD: Temporal Difference Learning
06. Function Approximation
07. PG: Policy Gradient
08. AC: Actor-Critic
09. DPG: Deterministic Policy Gradient
10. Maximum-Entropy RL
11. Policy-based Gradient-Free Algorithms
12. Distributional RL
13. Minimize Regret
14. Tree Search
15. IL and RLHF
16. More Agent-Environment Interface

**BibTeX**

    @book{xiao2023,
     title     = {Reinforcement Learning: Theory and {Python} Implementation},
     author    = {Zhiqing Xiao}
     year      = 2023,
     month     = 7,
     publisher = {China Machine Press},
    }

