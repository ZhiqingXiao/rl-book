# Reinforcement Learning: Theory and Python Implementation

**The First Reinforcement Learning Tutorial Book in English with one-on-one mapping TensorFlow 2 and PyTorch 1/2 Implementation**

**Cover RL algorithms for large models such as PPO, RLHF, IRL, and PbRL**

Please email me if you are interested in publishing this book in other languages.

### Features

This book comprehensively introduces the mainstream RL theory.

- This book introduces the trunk of the modern RL theory systematically. All major results are accompanied with proofs. We introduce the algorithms based on the theory, which covers all mainstream RL algorithms, including the algorithms in large model era such as PPO, RLHF, IRL, and PbRL.
- This book uses a consistent set of mathematical notations, which are compatible with mainstream RL tutorials.

All chapters are accompanied with Python codes.

- Easy to understand: All codes are implemented in a consistent and concise way, which directly maps to the explanation of algorithms.
- Easy to check: All codes and running results are shown in GitHub. We can either browse them in the web browser, or download locally to run them. Every algorithm is implemented in a self-contained standalone file, which can be browsed and executed individually.
- Diverse environments: We not only consider the built-in tasks in the library Gym, but also consider the third-party extension of the Gym. We even create environments for our own tasks.
- Highly compatible: All codes can be run in any one of all three major operating systems (Windows, macOS, and Linux). The methods to setup the environments are provided. Deep RL algorithms are implemented based on both TensorFlow 2 and PyTorch 1&2, so that readers can choose any one among the two or have a one-to-one comparison.
- Based on latest versions of software: All codes are based on the latest version of Python and its extension packages. The codes in GitHub will be updated according to the software update.
- Little hardware requirement: All codes can be run in a PC without GPU.

### Table of Contents

01. Introduction of Reinforcement Learning [view](https://doi.org/10.1007/978-981-19-4933-3_1)
02. Markov Decision Process [view](https://doi.org/10.1007/978-981-19-4933-3_2)
03. Model-based Numeric Iteration [view](https://doi.org/10.1007/978-981-19-4933-3_3)
04. MC: Monte-Carlo Learning [view](https://doi.org/10.1007/978-981-19-4933-3_4)
05. TD: Temporal Difference Learning [view](https://doi.org/10.1007/978-981-19-4933-3_5)
06. Function Approximation [view](https://doi.org/10.1007/978-981-19-4933-3_6)
07. PG: Policy Gradient [view](https://doi.org/10.1007/978-981-19-4933-3_7)
08. AC: Actor-Critic [view](https://doi.org/10.1007/978-981-19-4933-3_8)
09. DPG: Deterministic Policy Gradient [view](https://doi.org/10.1007/978-981-19-4933-3_9)
10. Maximum-Entropy RL [view](https://doi.org/10.1007/978-981-19-4933-3_10)
11. Policy-based Gradient-Free Algorithms [view](https://doi.org/10.1007/978-981-19-4933-3_11)
12. Distributional RL [view](https://doi.org/10.1007/978-981-19-4933-3_12)
13. Minimize Regret [view](https://doi.org/10.1007/978-981-19-4933-3_13)
14. Tree Search [view](https://doi.org/10.1007/978-981-19-4933-3_14)
15. More Agent-Environment Interface [view](https://doi.org/10.1007/978-981-19-4933-3_15)
16. Learning from Feedback and Imitation Learning [view](https://doi.org/10.1007/978-981-19-4933-3_16)

### Resources

- TOC, Table of notations, etc: [PDF in SpringerLink](https://link.springer.com/content/pdf/bfm:978-981-19-4933-3/1)
- Reference answers of multiple choices: [link](https://zhiqingxiao.github.io/rl-book/en2024/choice.html)
- Guide to set up developing environment: [Windows](https://github.com/ZhiqingXiao/rl-book/blob/master/en2024/setup/setupwin.md) [macOS](https://github.com/ZhiqingXiao/rl-book/blob/master/en2024/setup/setupmac.md)
- Table of abbreviations: [link](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/abbreviation.md)
- Table of algorithms: [link](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/algo.md)
- Table of interdisciplinary references: [link](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/iref.md)
- Table of figures: [link](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/figure.md)
- Table of tables: [link](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/table.md)
- Gym Internal: [link](https://github.com/ZhiqingXiao/rl-book/blob/master/en2024/gym.md)
- Bibliography: [link](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/bibliography.md)

### Table of Codes

List view: [link](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/code.md)

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
| 16 note | [HumanoidBulletEnv-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_ClosedForm_demo.html) | BehaviorClone [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_BC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_BC_torch.html), GAIL [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_GAILPPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_GAILPPO_torch.html) |


Note:
1. It does not work with Gym >=0.25 and PyBullet 3.2.4. It is because Gym 0.25 changed `metadata["render.modes"]` to `metadata["render_modes"]`, but PyBullet releases have not updated accordingly yet.


### BibTeX

    @book{xiao2024,
     title     = {Reinforcement Learning: Theory and {Python} Implementation},
     author    = {Zhiqing Xiao}
     year      = 2024,
     month     = 9,
     publisher = {Springer},
    }

# 强化学习：原理与Python实现（英文版）

**全球第一本配套 TensorFlow 2 和 PyTorch 1/2 一比一对照代码的英文强化学习书**

**解密大模型训练技术 PPO、RLHF、IRL和PbRL**

### 本书特色

本书完整地介绍了主流强化学习理论。
- 选用现代强化学习理论体系，突出主干，主要定理均给出证明过程。基于理论讲解强化学习算法，全面覆盖主流强化学习算法，包括了资格迹等经典算法和MuZero等深度强化学习算法。涵盖大模型时代的常用算法如PPO、RLHF、IRL、PbRL等。
- 全书采用完整的数学体系，各章内容循序渐进。全书采用一致的数学符号，并兼容主流强化学习教程。

本书各章均提供Python代码，实战性强。

- 简洁易懂：全书代码统一规范、简约完备，与算法讲解直接对应。
- 查阅方便：所有代码及运行结果均在GitHub上展示，既可以在浏览器上查阅，也可以下载到本地运行。各算法实现放在单独的文件里，可单独查阅和运行。
- 环境全面：既有Gym的内置环境，也有在Gym基础上进一步扩展的第三方环境，还带领读者一起实现自定义的环境。
- 兼容性好：所有代码在三大操作系统（Windows、macOS、Linux）上均可运行，书中给出了环境的安装和配置方法。深度强化学习代码还提供了TensorFlow 2和PyTorch 1/2对照代码。读者可任选其一。
- 版本新：全书代码基于最新版本的Python及其扩展库。作者会在GitHub上更新代码以适应版本升级。
- 硬件要求低：所有代码均可在没有GPU的个人计算机上运行。

### 代码

| 章 | 环境和闭式解 | 智能体 |
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
| 13 | [BernoulliMAB-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/en2024/code/BernoulliMABEnv_demo.html) |
| 13 | [GaussianMAB-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/en2024/code/GaussianMABEnv_demo.html) |
| 14 | [TicTacToe-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/TicTacToe-v0_ExhaustiveSearch.html) | AlphaZero [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/TicTacToe-v0_AlphaZero_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/TicTacToe-v0_AlphaZero_torch.html)  |
| 15 | [Tiger-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/Tiger-v0_ClosedForm.html) | [VI](https://zhiqingxiao.github.io/rl-book/en2024/code/Tiger-v0_Plan_demo.html)
| 16 注 | [HumanoidBulletEnv-v0](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_ClosedForm_demo.html) | BehaviorClone [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_BC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_BC_torch.html), GAIL [tf](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_GAILPPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/en2024/code/HumanoidBulletEnv-v0_GAILPPO_torch.html) |

注:
1. 此案例在 Gym >=0.25 且 PyBullet 3.2.4 的环境中无法工作。原因：Gym 0.25 把 `metadata["render.modes"]` 改成了 `metadata["render_modes"]`, 但是 PyBullet 未更新发行版。


### 中英双语资源

- 习题参考答案：[链接](https://zhiqingxiao.github.io/rl-book/en2024/choice.html)
- 开发环境搭建：[Windows](https://github.com/ZhiqingXiao/rl-book/blob/master/zh2023/setup/setupwin.md) [macOS](https://github.com/ZhiqingXiao/rl-book/blob/master/zh2023/setup/setupmac.md)
- 字母表：[链接](https://github.com/ZhiqingXiao/rl-book/blob/master/en2024/notation_zh.md)
- 缩略语表：[链接](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/abbreviation_zh.md)
- Gym源码解读：[链接](https://github.com/ZhiqingXiao/rl-book/blob/master/zh2023/gym.md)
- 参考文献：[链接](https://github.com/zhiqingxiao/rl-book/blob/master/en2024/bibliography.md)

**QQ群**

- QQ群：722846914（勘误报错可发此群，其他问题提问前请先Google，群主和管理员不提供免费咨询服务）

**常见问题**

- 问：Windows系统下安装TensorFlow或PyTorch失败。答：请在Windows 10/11里安装Visual Studio 2022（如果有旧版本的Visual Studio请先彻底卸载）。请阅读本书的[开发环境搭建指南](https://zhiqingxiao.github.io/rl-book/zh2023/setup/setupwin.html)。更多细节和安装问题请自行Google。PyTorch安装可参阅：https://mp.weixin.qq.com/s/uRx1XOPrfFOdMlRU6I-eyA

- 问：在Visual Studio或Visual Studio Code或PyCharm里面运行代码失败，比如找不到函数`display()`。答：本repo代码是配套Jupyter Notebook环境的，只能在Jupyter Notebook里运行。推荐您安装最新版本的Anaconda并直接运行下载来的Notebook。（`display()`函数是Jupyter Notebook里才有的函数。）不需要安装Visual Studio Code或PyCharm。更多细节或其他错误请自行Google。

- 问：GPU会比CPU跑的快么？答：没有用到TensorFlow和PyTorch的代码，不会用到GPU。用到TensorFlow和PyTorch的代码，由于网络一般不大，GPU反而可能更慢。PyTorch代码使用GPU时要把Tensor对象放在GPU上（可能需要修改代码）。

**热心读者 [Anesck](https://github.com/anesck) 对本书知识点的梳理评注（中文版）**

[第1章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/1.chapter_one.html) 
[第2章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/2.chapter_two.html) 
[第3章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/3.chapter_three.html) 
[第4章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/4.chapter_four.html) 
[第5章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/5.chapter_five.html) 
[第6章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/6.chapter_six.html) 
[第7章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/7.chapter_seven.html) 
[第8章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/8.chapter_eight.html) 
[第9章](https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/9.chapter_nine.html) 
