# 强化学习：原理与Python实现

**全球第一本配套 TensorFlow 2 代码的强化学习教程书**

**中国第一本配套 TensorFlow 2 代码的纸质算法书**

**现已提供 TensorFlow 2 和 PyTorch 1 [对照代码](https://zhiqingxiao.github.io/rl-book/#table-of-codes)**

![Book](https://zhiqingxiao.github.io/images/book/rl.jpg)

本书介绍强化学习理论及其 Python 实现。
- 理论完备：全书用一套完整的数学体系，严谨地讲授强化学习的理论基础，主要定理均给出证明过程。各章内容循序渐进，覆盖了所有主流强化学习算法，包括资格迹等非深度强化学习算法和柔性执行者/评论者等深度强化学习算法。
- 案例丰富：在您最爱的操作系统（包括 Windows、macOS、Linux）上，基于 Python 3.10、Gym 0.23 和 TensorFlow 2 / PyTorch 1，实现强化学习算法。全书实现统一规范，体积小、重量轻。第 1～9 章给出了算法的配套实现，环境部分只依赖于 Gym 的最小安装，在没有 GPU 的计算机上也可运行；第 10～12 章介绍了多个热门综合案例，涵盖 Gym 的完整安装和自定义扩展，在有普通 GPU 的计算机上即可运行。

**2020年更新**

本书深度强化学习部分新增 [基于 TensorFlow 2 和 PyTorch 1 的算法对照实现](https://zhiqingxiao.github.io/rl-book/#table-of-codes)。
两个版本实现均和正文伪代码严格对应，两个版本仅在智能体部分实现不同，程序结构和智能体参数完全相同。

**2022年更新**

由于GitHub更改了Jupyter Notebook的显示方式为默认不显示输出，所以我将Jupyter Notebook转成了HTML文件，存在./html文件夹下以方便查阅程序输出。


### 目录

01. 初识强化学习 &emsp; [查看代码：useGym](https://github.com/zhiqingxiao/rl-book/blob/master/chapter01_intro/useGym.ipynb)
02. Markov决策过程 &emsp; [查看代码：useBellman](https://github.com/zhiqingxiao/rl-book/blob/master/chapter02_mdp/useBellman.ipynb) [CliffWalking](https://github.com/zhiqingxiao/rl-book/blob/master/chapter02_mdp/CliffWalking-v0.ipynb)
03. 有模型数值迭代 &emsp; [查看代码：FrozenLake](https://github.com/zhiqingxiao/rl-book/blob/master/chapter03_dp/FrozenLake-v1.ipynb)
04. 回合更新价值迭代 &emsp; [查看代码：Blackjack](https://github.com/zhiqingxiao/rl-book/blob/master/chapter04_mc/Blackjack-v1.ipynb)
05. 时序差分价值迭代 &emsp; [查看代码：Taxi](https://github.com/zhiqingxiao/rl-book/blob/master/chapter05_td/Taxi-v3.ipynb)
06. 函数近似方法 &emsp; [查看代码：MountainCar](https://github.com/zhiqingxiao/rl-book/blob/master/chapter06_approx/MountainCar-v0_tf.ipynb)
07. 回合更新策略梯度方法 &emsp; [查看代码：CartPole](https://github.com/zhiqingxiao/rl-book/blob/master/chapter07_pg/CartPole-v0_tf.ipynb)
08. 执行者/评论者方法 &emsp; [查看代码：Acrobot](https://github.com/zhiqingxiao/rl-book/blob/master/chapter08_ac/Acrobot-v1_tf.ipynb)
09. 连续动作空间的确定性策略 &emsp; [查看代码：Pendulum](https://github.com/zhiqingxiao/rl-book/blob/master/chapter09_dpg/Pendulum-v1_tf.ipynb)
10. 综合案例：电动游戏 &emsp; [查看代码：Breakout](https://github.com/zhiqingxiao/rl-book/blob/master/chapter10_atari/BreakoutDeterministic-v4_tf.ipynb) [Pong](https://github.com/zhiqingxiao/rl-book/blob/master/chapter10_atari/PongDeterministic-v4_tf.ipynb) [Seaquest](https://github.com/zhiqingxiao/rl-book/blob/master/chapter10_atari/SeaquestDeterministic-v4_tf.ipynb)
11. 综合案例：棋盘游戏 &emsp; [查看代码：TicTacToe](https://github.com/zhiqingxiao/rl-book/blob/master/chapter11_alphazero/TicTacToe-v0_tf.ipynb) [Reversi](https://github.com/zhiqingxiao/rl-book/blob/master/chapter11_alphazero/Reversi-v0_4x4_tf.ipynb) [boardgame2](https://github.com/zhiqingxiao/boardgame2)
12. 综合案例：自动驾驶 &emsp; [查看代码：AirSimNH](https://github.com/zhiqingxiao/rl-book/blob/master/chapter12_drive/AirSimNH_tf.ipynb)

**QQ群**

- QQ群：948110103（勘误报错可发此群，其他问题提问前请先Google，群主和管理员不提供免费咨询服务）
- 多任务群：696984257（非小白群，多任务强化学习+强化元学习+终身强化学习+迁移强化学习，勘误报错勿发此群，提问前请先Google）
- 关于入群验证问题：由于QQ的bug，即使正确输入答案，也可能会验证失败。这时更换设备重试、更换输入法重试、改日重试均可能解决问题。如果答案中有英文字母，清注意大小写。
- 纸板书前言中给出的QQ群（935702193和243613392）已满，不再新增群成员，谢谢理解。

**书籍勘误与更新**
- 2019年08月第1版第1次印刷：[查看勘误与更新](https://zhiqingxiao.github.io/rl-book/errata/errata201908.html) 拼多多上的盗版都是这个版次的，建议退掉，然后到天猫/京东/当当上买新版
- 2019年11月第1版第2次印刷：[查看勘误与更新](https://zhiqingxiao.github.io/rl-book/errata/errata201911.html)
- 2019年12月第1版第3次印刷：[查看勘误与更新](https://zhiqingxiao.github.io/rl-book/errata/errata201912.html)
- 2020年09月第1版第4次印刷：[查看勘误与更新](https://zhiqingxiao.github.io/rl-book/errata/errata202009.html)
- 2020年11月第1版第5次印刷：[查看勘误与更新](https://zhiqingxiao.github.io/rl-book/errata/errata202011.html)
- 2021年01月第1版第6次印刷：[查看勘误与更新](https://zhiqingxiao.github.io/rl-book/errata/errata202101.html)
- 2021年10月第1版第7次印刷：[查看勘误与更新](https://zhiqingxiao.github.io/rl-book/errata/errata202110.html)
- 电子版不提供勘误与更新。

**判断纸质版书籍版次的方法 / 确定纸质书印刷时间的方法**
- “前言”之前有1页是“图书在版编目（CIP）数据”。这页下部的表格中有一项是“版次”，该项标明当前书是什么时候第几次印刷的。

**本书数学符号表**
- [下载PDF](https://raw.githubusercontent.com/zhiqingxiao/rl-book/master/resources/notations.pdf)

**本书电子版**

本书不仅有纸质版销售，也有电子版销售。不过，电子版没有提供配套的勘误与更新资源，而且公式展示不美观，对阅读带来困难。所以推荐购买纸质版。电子版销售平台包括但不限于：
- Kindle电子书：https://www.amazon.cn/dp/B07X936G34/
- 京东读书：https://e.jd.com/30513215.html
- 华章课堂：http://www.hzcourse.com/web/refbook/detail/8397/226

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

- 问：运行的结果和repo里带的结果不完全一样。答：本repo中涉及到TensorFlow或PyTorch的代码，附带的结果都是用CPU跑的。GPU运算本来就不能精确复现（更多细节请自行Google）。Gym 0.22版本重新实现了seeding机制，有些结果是用Gym <=0.21版本跑的，而没有用Gym 0.22重跑。如果发现Gym 0.22 CPU版本运行结果不正常请发送勘误报错，谢谢。

- 问：GPU会比CPU跑的快么？答：没有用到TensorFlow和PyTorch的代码，不会用到GPU。用到TensorFlow和PyTorch的代码，由于网络一般不大，GPU反而可能更慢。PyTorch代码使用GPU时要把Tensor对象放在GPU上（可能需要修改代码）。

# Reinforcement Learning: Theory and Python Implementation

**The First Reinforcement Learning Tutorial Book with TensorFlow 2 Implementation**

**[Codes](https://github.com/ZhiqingXiao/rl-book/tree/master/notebooks) with both TensorFlow 2 and PyTorch 1**

This is a tutorial book on reinforcement learning, with explanation of theory and Python implementation.
- Theory: Starting from a uniform mathematical framework, this book derives the theory and algorithms of reinforcement learning, including all major algorithms such as eligibility traces and soft actor-critic algorithms.
- Practice: Every chapter is accompanied by high quality implementation based on Python 3.10, Gym 0.23, and TensorFlow 2 / PyTorch 1. Codes in first 9 chapters only depends on minimum installation of Gym, and can be run in a laptop without GPU. Codes in the last 3 chapters can be run in a laptop with a normal GPU. All codes are compatible with Windows, Linux, and macOS.


**Please email me if you are interested in publishing this book in other languages.** English version will be published by Springer Nature.


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

### Table of Contents

[Detail](https://raw.githubusercontent.com/zhiqingxiao/rl-book/master/resources/toc.pdf)

01. Introduction of Reinforcement Learning
02. Markov Decision Process
03. Model-based Numeric Iteration
04. Monte-Carlo Learning
05. Temporal Difference Learning
06. Function Approximation
07. Policy Gradient
08. Actor-Critic
09. Deterministic Policy Gradient
10. Case Study: Video Game
11. Case Study: Board Game
12. Case Study: Autonomous Driving


**BibTeX**

    @book{xiao2019,
     title     = {Reinforcement Learning: Theory and {Python} Implementation},
     author    = {Zhiqing Xiao}
     year      = 2019,
     month     = 8,
     publisher = {China Machine Press},
    }

