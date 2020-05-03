# 强化学习：原理与Python实现

**世界上第一本配套 TensorFlow 2 代码的强化学习教程书**

**中国第一本配套 TensorFlow 2 代码的纸质算法书**

![Book](https://zhiqingxiao.github.io/images/book/rl.jpg)

本书介绍强化学习理论及其 Python 实现。
- 理论完备：全书用一套完整的数学体系，严谨地讲授强化学习的理论基础，主要定理均给出证明过程。各章内容循序渐进，覆盖了所有主流强化学习算法，包括资格迹等非深度强化学习算法和柔性执行者/评论者等深度强化学习算法。
- 案例丰富：在您最爱的操作系统（包括 Windows、macOS、Linux）上，基于最新的 Python 3.7、Gym 0.17 和 TensorFlow 2.1（兼容 TensorFlow 1.15），实现强化学习算法。全书实现统一规范，体积小、重量轻。第 1～9 章给出了算法的配套实现，环境部分只依赖于 Gym 的最小安装，在没有 GPU 的计算机上也可运行；第 10～12 章介绍了多个热门综合案例，涵盖 Gym 的完整安装和自定义扩展，在有普通 GPU 的计算机上即可运行。


### 目录

01. 初识强化学习 &emsp; [查看代码：useGym](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter01_intro/useGym.ipynb)
02. Markov决策过程 &emsp; [查看代码：useBellman](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter02_mdp/useBellman.ipynb) [CliffWalking](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter02_mdp/CliffWalking-v0.ipynb)
03. 有模型数值迭代 &emsp; [查看代码：FrozenLake](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter03_dp/FrozenLake-v0.ipynb)
04. 回合更新价值迭代 &emsp; [查看代码：Blackjack](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter04_mc/Blackjack-v0.ipynb)
05. 时序差分价值迭代 &emsp; [查看代码：Taxi](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter05_td/Taxi-v3.ipynb)
06. 函数近似方法 &emsp; [查看代码：MountainCar](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter06_approx/MountainCar-v0_tf.ipynb)
07. 回合更新策略梯度方法 &emsp; [查看代码：CartPole](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter07_pg/CartPole-v0_tf.ipynb)
08. 执行者/评论者方法 &emsp; [查看代码：Acrobot](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter08_ac/Acrobot-v1_tf.ipynb)
09. 连续动作空间的确定性策略 &emsp; [查看代码：Pendulum](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter09_dpg/Pendulum-v0_tf.ipynb)
10. 综合案例：电动游戏 &emsp; [查看代码：Breakout](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter10_atari/BreakoutDeterministic-v4_tf.ipynb) [Pong](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter10_atari/PongDeterministic-v4_tf.ipynb) [Seaquest](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter10_atari/SeaquestDeterministic-v4_tf.ipynb)
11. 综合案例：棋盘游戏 &emsp; [查看代码：TicTacToe](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter11_alphazero/TicTacToe-v0_tf.ipynb) [Reversi](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter11_alphazero/Reversi-v0_4x4_tf.ipynb) [boardgame2](https://github.com/zhiqingxiao/boardgame2)
12. 综合案例：自动驾驶 &emsp; [查看代码：AirSimNH](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/chapter12_drive/AirSimNH_tf.ipynb)

**QQ群**
- 群号：935702193 （免费入群）
- 关于入群验证问题：由于QQ的bug，即使正确输入答案，也可能会验证失败。这时更换设备重试、更换输入法重试、改日重试均可能解决问题。如果答案中有英文字母，清注意大小写。人名的首字母应大写。

**书籍勘误与更新**
- 2019年08月第1版第1次印刷：[查看勘误与更新](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/errata/errata201908.ipynb)
- 2019年11月第1版第2次印刷：[查看勘误与更新](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/errata/errata201911.ipynb)
- 2019年12月第1版第3次印刷：[查看勘误与更新](https://nbviewer.jupyter.org/github/zhiqingxiao/rl-book/blob/master/errata/errata201912.ipynb)
- 电子版不提供勘误与更新。

**判断纸质版书籍版次的方法 / 确定纸质书印刷时间的方法**
- “前言”之前有1页是“图书在版编目（CIP）数据”。这页下部的表格中有一项是“版次”，该项标明当前书是什么时候第几次印刷的。

**本书数学符号表**
- [下载PDF](https://raw.githubusercontent.com/zhiqingxiao/rl-book/master/notations.pdf)

**本书电子版**

本书不仅有纸质版销售，也有电子版销售。不过，电子版没有提供配套的勘误与更新资源，所以推荐购买纸质版。电子版销售平台包括但不限于：
- 华章鲜读：微信订阅公众号“华章电子书”，“在线书城”，搜索“强化学习”，在“鲜读”栏目下找到本书
- Kindle电子书：https://www.amazon.cn/dp/B07X936G34/
- 京东读书：https://e.jd.com/30513215.html
- 知乎书店：https://www.zhihu.com/pub/reader/119634282


# Reinforcement Learning: Theory and Python Implementation

**The First Reinforcement Learning Tutorial Book with TensorFlow 2 Implementation**

This is a tutorial book on reinforcement learning, with explanation of theory and Python implementation.
- Theory: Starting from a uniform mathematical framework, this book derives the theory and algorithms of reinforcement learning, including all major algorithms such as eligibility traces and soft actor-critic algorithms.
- Practice: Every chapter is accompanied by high quality implementation based on Python 3.7, Gym 0.17, and TensorFlow 2.1.

### Table of Contents

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
12. Case Study: Self-Driving Car


**BibTeX**

    @book{xiao2019,
     title     = {Reinforcement Learning: Theory and {Python} Implementation},
     author    = {Zhiqing Xiao}
     year      = 2019,
     month     = 8,
     publisher = {China Machine Press},
    }

