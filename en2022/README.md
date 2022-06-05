# Reinforcement Learning: Theory and Python Implementation

**The First Reinforcement Learning Tutorial Book with one-on-one mapping TensorFlow 2 and PyTorch 1 Implementation**

**[Codes](https://github.com/ZhiqingXiao/rl-book/tree/master/notebooks) with both TensorFlow 2 and PyTorch 1**

**Please email me if you are interested in publishing this book in other languages.**

### Features

This book comprehensively introduces the mainstream RL theory.

- This book introduces the trunk of the modern RL theory in a systematically way. All major results are accompanied with proofs. We introduce the algorithms based on the theory, which covers all mainstream RL algorithms, including both classical RL algorithms such as eligibility trace and deep RL algorithm such as MuZero.
- This book uses a consistent set of mathematical notations, which are compatible with mainstream RL tutorials.

All chapters are accompanied with Python codes.

- Easy to understand: All codes are implemented in a consistent and concise way, which directly maps to the explanation of algorithms.
- Easy to check: All codes and running results are shown in GitHub. We can either browse them in the web browser, or download locally to run them. Every algorithm is implemented in a self-contained standalone file, which can be browsed and executed individually.
- Diverse environments: We not only consider the built-in tasks in the library Gym, but also consider the third-party extension of the Gym. We even create environments for our own tasks.
- Highly compatible: All codes can be run in any one of all three major operating systems (Windows, macOS, and Linux). The methods to setup the environments are provided. Deep RL algorithms are implemented based on both TensorFlow 2 and PyTorch 1, so that readers can choose any one among the two or have a one-to-one comparison.
- Based on latest versions of software: All codes are based on the latest version of Python and its extension packages. The codes in GitHub will be updated according to the software update.
- Little hardware requirement: All codes can be run in a PC without GPU.

### Table of Contents

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
15. IL: Imitation Learning
16. More Agent-Environment Interface

### Table of Codes

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
| 12 | [PongNoFrameskip-v4](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_ClosedForm.html) | CategoricalDQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_CategoricalDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_CategoricalDQN_torch.html), QR-DQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_QRDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_QRDQN_torch.html), IQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_IQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_IQN_torch.html) |
| 13 | [BernoulliMAB-v0](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) |
| 13 | [GaussianMAB-v0](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/html/GaussianMABEnv_demo.html) |
| 14 | [TicTacToe-v0](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_ExhaustiveSearch.html) | AlphaZero [tf](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_AlphaZero_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_AlphaZero_torch.html)  |
| 15 | [HumanoidBulletEnv-v0](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_ClosedForm_demo.html) | BehaviorClone [tf](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_BC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_BC_torch.html), GAIL [tf](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_GAILPPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_GAILPPO_torch.html) |
| 16 | [Tiger-v0](https://zhiqingxiao.github.io/rl-book/html/Tiger-v0_ClosedForm.html) | [VI](https://zhiqingxiao.github.io/rl-book/html/Tiger-v0_planning_demo.html)

**Exercise**

[Reference Answers for Multiple Choices](https://zhiqingxiao.github.io/rl-book/en2022/exercise/choice.html)

**BibTeX**

    @book{xiao2022,
     title     = {Reinforcement Learning: Theory and {Python} Implementation},
     author    = {Zhiqing Xiao}
     year      = 2022,
     publisher = {Springer Nature},
    }

# 强化学习：原理与Python实现（英文版）

**全球第一本配套TensorFlow 2和PyTorch 1一比一对照代码的强化学习书**

**本书特色**

本书完整地介绍了主流强化学习理论。
- 	选用现代强化学习理论体系，突出主干，主要定理均给出证明过程。基于理论讲解强化学习算法，全面覆盖主流强化学习算法，包括了资格迹等经典算法和MuZero等深度强化学习算法。
- 全书采用完整的数学体系，各章内容循序渐进。全书采用一致的数学符号，并兼容主流强化学习教程。

本书各章均提供Python代码，实战性强。

- 简洁易懂：全书代码统一规范、简约完备，与算法讲解直接对应。
- 查阅方便：所有代码及运行结果均在GitHub上展示，既可以在浏览器上查阅，也可以下载到本地运行。各算法实现放在单独的文件里，可单独查阅和运行。
- 环境全面：既有Gym的内置环境，也有在Gym基础上进一步扩展的第三方环境，还带领读者一起实现自定义的环境。
- 兼容性好：所有代码在三大操作系统（Windows、macOS、Linux）上均可运行，书中给出了环境的安装和配置方法。深度强化学习代码还提供了TensorFlow 2和PyTorch 1对照代码。读者可任选其一。
- 版本新：全书代码基于最新版本的Python及其扩展库。作者会在GitHub上更新代码以适应版本升级。
- 硬件要求低：所有代码均可在没有GPU的个人计算机上运行。

### 代码

| 章 | 环境和闭式解 | 智能体 |
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
| 12 | [PongNoFrameskip-v4](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_ClosedForm.html) | CategoricalDQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_CategoricalDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_CategoricalDQN_torch.html), QR-DQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_QRDQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_QRDQN_torch.html), IQN [tf](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_IQN_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/PongNoFrameskip-v4_IQN_torch.html) |
| 13 | [BernoulliMAB-v0](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) |
| 13 | [GaussianMAB-v0](https://zhiqingxiao.github.io/rl-book/html/BernoulliMABEnv_demo.html) | [UCB](https://zhiqingxiao.github.io/rl-book/html/GaussianMABEnv_demo.html) |
| 14 | [TicTacToe-v0](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_ExhaustiveSearch.html) | AlphaZero [tf](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_AlphaZero_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/TicTacToe-v0_AlphaZero_torch.html)  |
| 15 | [HumanoidBulletEnv-v0](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_ClosedForm_demo.html) | BehaviorClone [tf](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_BC_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_BC_torch.html), GAIL [tf](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_GAILPPO_tf.html) [torch](https://zhiqingxiao.github.io/rl-book/html/HumanoidBulletEnv-v0_GAILPPO_torch.html) |
| 16 | [Tiger-v0](https://zhiqingxiao.github.io/rl-book/html/Tiger-v0_ClosedForm.html) | [VI](https://zhiqingxiao.github.io/rl-book/html/Tiger-v0_planning_demo.html)

**习题**

[单选题参考答案](https://zhiqingxiao.github.io/rl-book/en2022/exercise/choice.html)

**QQ群**

- QQ群：722846914（勘误报错可发此群，其他问题提问前请先Google，群主和管理员不提供免费咨询服务）

**常见问题**

- 问：Windows系统下安装TensorFlow或PyTorch失败。答：请在Windows 10/11里安装Visual Studio 2022（如果有旧版本的Visual Studio请先彻底卸载）。更多细节和安装问题请自行Google。PyTorch安装可参阅：https://mp.weixin.qq.com/s/uRx1XOPrfFOdMlRU6I-eyA

- 问：在Visual Studio或Visual Studio Code或PyCharm里面运行代码失败，比如找不到函数`display()`。答：本repo代码是配套Jupyter Notebook环境的，只能在Jupyter Notebook里运行。推荐您安装最新版本的Anaconda并直接运行下载来的Notebook。（`display()`函数是Jupyter Notebook里才有的函数。）不需要安装Visual Studio Code或PyCharm。更多细节或其他错误请自行Google。

- 问：运行的结果和repo里带的结果不完全一样。答：本repo中涉及到TensorFlow或PyTorch的代码，附带的结果都是用CPU跑的。GPU运算本来就不能精确复现（更多细节请自行Google）。如果发现Gym最新版CPU版本运行结果不正常请发送勘误报错，谢谢。

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
