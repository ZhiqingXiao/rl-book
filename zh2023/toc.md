目录 Table of Contents
----

|   |   |   |
| :--- | :--- | :--- |
| **1.** | **初识强化学习** | **Introduction of Reinforcement Learning (RL)** |
| 1.1. | 强化学习及其关键元素 | What is RL? |
| 1.2. | 强化学习的应用 | Applications of RL |
| 1.3. | 智能体/环境接口 | Agent–Environment Interface |
| 1.4. | 强化学习的分类 | Taxonomy of RL |
| 1.4.1. | 按算法分类 | Task-based Taxonomy |
| 1.4.2. | 按任务分类 | Algorithm-based Taxonomy |
| 1.5. | 强化学习的性能指标 | Performance Metrics |
| 1.6. | 案例：基于Gym库的智能体/环境接口 | Case Study: Agent–Environment Interface in Gym |
| 1.6.1. | 安装Gym库 | Install Gym |
| 1.6.2. | 使用Gym库 | Use Gym |
| 1.6.3. | 小车上山 | Example: MountainCar |
| 1.7. | 本章小结 | Summary |
| 1.8. | 练习题 | Exercises |
|  |  |  |
| **2.** | **Markov决策过程** | **MDP: Markov Decision Process** |
| 2.1. | Markov决策过程模型 | MDP Model |
| 2.1.1. | 离散时间Markov决策过程 | DTMDP: Discrete-Time MDP |
| 2.1.2. | 环境与动力 | Environment and Dynamics |
| 2.1.3. | 策略 | Policy |
| 2.1.4. | 带折扣的回报 | Discounted Return |
| 2.2. | 价值 | Value |
| 2.2.1. | 价值的定义 | Definition of Value |
| 2.2.2. | 价值的性质 | Properties of Values |
| 2.2.3. | 策略的偏序和改进 | Partial Order of Policy and Policy Improvement |
| 2.3. | 带折扣的分布 | Discounted Visitation Frequency |
| 2.3.1. | 带折扣的分布的定义 | Definition of Discounted Visitation Frequency |
| 2.3.2. | 带折扣的分布的性质 | Properties of Discounted Visitation Frequency |
| 2.3.3. | 带折扣的分布和策略的等价性 | Equivalence between Discounted Visitation Frequency and Policy |
| 2.3.4. | 带折扣的分布下的期望 | Expectation over Discounted Distribution |
| 2.4. | 最优策略与最优价值 | Optimal Policy and Optimal Value |
| 2.4.1. | 从最优策略到最优价值 | From Optimal Policy to Optimal Value |
| 2.4.2. | 最优策略的存在性 | Existence of Optimal Policy |
| 2.4.3. | 最优价值的性质与Bellman最优方程 | Properties of Optimal Values and Bellman Optimal Equations |
| 2.4.4. | 线性规划法求解最优价值 | LP: Linear Programming Method |
| 2.4.5. | 用最优价值求解最优策略 | Use Optimal Values to Find Optimal Strategy |
| 2.5. | 案例：悬崖寻路 | Case Study: CliffWalking |
| 2.5.1. | 使用环境 | Use Environment |
| 2.5.2. | 求解策略价值 | Policy Evaluation |
| 2.5.3. | 求解最优价值 | Solve Optimal Values |
| 2.5.4. | 求解最优策略 | Solve Optimal Policy |
| 2.6. | 本章小结 | Summary |
| 2.7. | 练习题 | Exercises |
|  |  |  |
| **3.** | **有模型数值迭代** | **Model-based Numerical Iteration** |
| 3.1. | Bellman算子及其性质 | Bellman Operators and Its Properties |
| 3.2. | 有模型策略迭代 | Model-based Policy Iteration |
| 3.2.1. | 策略评估 | Policy Evaluation |
| 3.2.2. | 策略改进 | Policy Improvement |
| 3.2.3. | 策略迭代 | Policy Iteration |
| 3.3. | 价值迭代 | VI: Value Iteration |
| 3.4. | 自益与动态规划 | Bootstrapping and Dynamic Programming |
| 3.5. | 案例：冰面滑行 | Case Study: FrozenLake |
| 3.5.1. | 使用环境 | Use Environment |
| 3.5.2. | 有模型策略迭代求解 | Model-based Policy Iteration |
| 3.5.3. | 有模型价值迭代求解 | Model-based VI |
| 3.6. | 本章小结 | Summary |
| 3.7. | 练习题 | Exercises |
|  |  |  |
| **4.** | **回合更新价值迭代** | **MC: Monte Carlo Learning** |
| 4.1. | 同策回合更新 | On-Policy MC Learning |
| 4.1.1. | 同策回合更新策略评估 | On-Policy MC Policy Evaluation |
| 4.1.2. | 带起始探索的同策回合更新 | MC Learning with Exploration Start |
| 4.1.3. | 基于柔性策略的同策回合更新 | MC Learning on Soft Policy |
| 4.2. | 异策回合更新 | Off-Policy MC Learning |
| 4.2.1. | 重要性采样 | Importance Sampling |
| 4.2.2. | 异策回合更新策略评估 | Off-Policy MC Policy Evaluation |
| 4.2.3. | 异策回合更新最优策略求解 | Off-Policy MC Policy Optimization |
| 4.3. | 实验：21点游戏 | Case Study: Blackjack |
| 4.3.1. | 使用环境 | Use Environment |
| 4.3.2. | 同策策略评估 | On-Policy Policy Evaluation |
| 4.3.3. | 同策最优策略求解 | On-Policy Policy Optimization |
| 4.3.4. | 异策策略评估 | Off-Policy Policy Evaluation |
| 4.3.5. | 异策最优策略求解 | Off-Policy Policy Optimization |
| 4.4. | 本章小结 | Summary |
| 4.5. | 练习题 | Exercises |
|  |  |  |
| **5.** | **时序差分价值迭代** | **TD: Temporal Difference Learning** |
| 5.1. | 时序差分目标 | TD return |
| 5.2. | 同策时序差分更新 | On-Policy TD Learning |
| 5.2.1. | 时序差分更新策略评估 | TD Policy Evaluation |
| 5.2.2. | SARSA算法 | SARSA |
| 5.2.3. | 期望SARSA算法 | Expected SARSA |
| 5.3. | 异策时序差分更新 | Off-Policy TD Learning |
| 5.3.1. | 基于重要性采样的异策算法 | Off-Policy Algorithm based on Importance Sampling |
| 5.3.2. | Q学习 | Q Learning |
| 5.3.3. | 双重Q学习 | Double Q Learning |
| 5.4. | 资格迹 | Eligibility Trace |
| 5.4.1. | $\lambda$ 回报 | $\lambda$ Return |
| 5.4.2. | TD( $\lambda$ ) | TD( $\lambda$ ) |
| 5.5. | 案例：的士调度 | Case Study: Taxi |
| 5.5.1. | 使用环境 | Use Environment |
| 5.5.2. | 同策时序差分学习 | On-Policy TD |
| 5.5.3. | 异策时序差分学习 | Off-Policy TD |
| 5.5.4. | 资格迹学习 | Eligibility Trace |
| 5.6. | 本章小结 | Summary |
| 5.7. | 练习题 | Exercises |
|  |  |  |
| **6.** | **函数近似方法** | **Function Approximation** |
| 6.1. | 函数近似原理 | Basic of Function Approximation |
| 6.2. | 基于梯度的参数更新 | Parameter Update using Gradient |
| 6.2.1. | 随机梯度下降 | SGD: Stochastic Gradient Descent |
| 6.2.2. | 半梯度下降 | Semi-Gradient Descent |
| 6.2.3. | 带资格迹的半梯度下降 | Semi-Gradient Descent with Eligibility Trace |
| 6.3. | 函数近似的收敛性 | Convergence of Function Approximation |
| 6.3.1. | 收敛的条件 | Condition of Convergence |
| 6.3.2. | Baird反例 | Baird’s Counterexample |
| 6.4. | 深度Q网络 | DQN: Deep Q Network |
| 6.4.1. | 经验回放 | Experience Replay |
| 6.4.2. | 目标网络 | Deep Q Learning with Target Network |
| 6.4.3. | 双重深度Q网络 | Double DQN |
| 6.4.4. | 决斗深度Q网络 | Dueling DQN |
| 6.5. | 案例：小车上山 | Case Study: MountainCar |
| 6.5.1. | 使用环境 | Use Environment |
| 6.5.2. | 用线性近似求解最优策略 | Linear Approximation |
| 6.5.3. | 用深度Q网络求解最优策略 | DQN and its Variants |
| 6.6. | 本章小结 | Summary |
| 6.7. | 练习题 | Exercises |
|  |  |  |
| **7.** | **回合更新策略梯度方法** | **PG: Policy Gradient** |
| 7.1. | 策略梯度算法的原理 | Theory of PG |
| 7.1.1. | 函数近似策略 | Function Approximation for Policy |
| 7.1.2. | 策略梯度定理 | PG Theorem |
| 7.1.3. | 策略梯度和极大似然估计的关系 | Relationship between PG and Maximum Likelihood Estimate |
| 7.2. | 同策回合更新策略梯度算法 | On-Policy PG |
| 7.2.1. | 简单的策略梯度算法 | VPG: Vanilla Policy Gradient |
| 7.2.2. | 带基线的简单策略梯度算法 | PG with Baseline |
| 7.3. | 异策回合更新策略梯度算法 | Off-Policy PG |
| 7.4. | 案例：车杆平衡 | Case Study: CartPole |
| 7.4.1. | 同策策略梯度算法求解最优策略 | On-Policy PG |
| 7.4.2. | 异策策略梯度算法求解最优策略 | Off-Policy PG |
| 7.5. | 本章小结 | Summary |
| 7.6. | 练习题 | Exercises |
|  |  |  |
| **8.** | **执行者/评论者** | **AC: Actor–Critic** |
| 8.1. | 执行者/评论者方法 | Intuition of AC |
| 8.2. | 同策执行者/评论者算法 | On-Policy AC |
| 8.2.1. | 动作价值执行者/评论者算法 | Action-Value AC |
| 8.2.2. | 优势执行者/评论者算法 | Advantage AC |
| 8.2.3. | 带资格迹的执行者/评论者算法 | Eligibility Trace AC |
| 8.3. | 基于代理优势的同策算法 | On-Policy AC with Surrogate Objective |
| 8.3.1. | 性能差别引理 | Performance Difference Lemma |
| 8.3.2. | 代理优势 | Surrogate Advantage |
| 8.3.3. | 邻近策略优化 | PPO: Proximal Policy Optimization |
| 8.4. | 自然梯度和信赖域算法 | Natural PG and Trust Region Algorithm |
| 8.4.1. | KL散度与Fisher信息矩阵 | Kullback-Leibler Divergence and Fisher Information Matrix |
| 8.4.2. | 代理优势的信赖域 | Trust Region of Surrogate Objective |
| 8.4.3. | 自然策略梯度算法 | NPG: Natural Policy Gradient |
| 8.4.4. | 信赖域策略优化 | TRPO: Trust Region Policy Optimization |
| 8.5. | 重要性采样异策执行者/评论者算法 | Importance Sampling Off-policy AC |
| 8.6. | 案例：双节倒立摆 | Case Study: Acrobot |
| 8.6.1. | 同策执行者/评论者算法求解最优策略 | On-Policy AC |
| 8.6.2. | 基于代理优势的同策算法求解最优策略 | On-Policy AC with Surrogate Objective |
| 8.6.3. | 自然策略梯度和信赖域算法求解最优策略 | NPG and TRPO |
| 8.6.4. | 重要性采样异策执行者/评论者算法求解最优策略 | Importance Sampling Off-Policy PG |
| 8.7. | 本章小结 | Summary |
| 8.8. | 练习题 | Exercises |
|  |  |  |
| **9.** | **连续动作空间的确定性策略** | **DPG: Deterministic Policy Gradient** |
| 9.1. | 确定性策略梯度定理 | DPG Theorem |
| 9.2. | 同策确定性算法 | On-Policy DPG |
| 9.3. | 异策确定性算法 | Off-Policy DPG |
| 9.3.1. | 基本的异策确定性执行者/评论者算法 | OPDAC: Off-Policy Deterministic Actor–Critic |
| 9.3.2. | 深度确定性策略梯度算法 | DDPG: Deep Deterministic Policy Gradient |
| 9.3.3. | 双重延迟深度确定性策略梯度算法 | TD3: Twin Delay Deep Deterministic Policy Gradient |
| 9.4. | 探索过程 | Exploration Process |
| 9.5. | 案例：倒立摆的控制 | Case Study: Pendulum |
| 9.5.1. | 用深度确定性策略梯度算法求解 | DDPG |
| 9.5.2. | 用双重延迟深度确定性算法求解 | TD3 |
| 9.6. | 本章小结 | Summary |
| 9.7. | 练习题 | Exercises |
|  |  |  |
| **10.** | **最大熵强化学习** | **Maximum-Entropy RL** |
| 10.1. | 最大熵强化学习与柔性强化学习理论 | Maximum-Entropy RL and Soft RL |
| 10.1.1. | 奖励工程和带熵的奖励 | Reward Engineering and Reward with Entropy |
| 10.1.2. | 柔性价值 | Soft Values |
| 10.1.3. | 柔性策略改进定理和最大熵强化学习的迭代求解 | Soft Policy Improvement Theorem and Numeric Iterative Algorithm |
| 10.1.4. | 柔性最优价值 | Optimal Values |
| 10.1.5. | 柔性策略梯度定理 | Soft Policy Gradient Theorem |
| 10.2. | 柔性强化学习算法 | Soft RL Algorithms |
| 10.2.1. | 柔性Q学习 | SQL: Soft Q Learning |
| 10.2.2. | 柔性执行者/评论者算法 | SAC: Soft Actor–Critic |
| 10.3. | 自动熵调节 | Automatic Entropy Adjustment |
| 10.4. | 案例：月球登陆器 | Case Study: Lunar Lander |
| 10.4.1. | 环境安装 | Install Environment |
| 10.4.2. | 使用环境 | Use Environment |
| 10.4.3. | 用柔性Q学习求解LunarLander | Use SQL to Solve LunarLander |
| 10.4.4. | 用柔性执行者/评论者求解LunarLander | Use SAC to Solve LunarLander |
| 10.4.5. | 自动熵调节用于LunarLander | Use Automatic Entropy Adjustment to Solve LunarLander |
| 10.4.6. | 求解LunarLanderContinuous | Solve LunarLanderContinuous |
| 10.5. | 本章小结 | Summary |
| 10.6. | 练习题 | Exercises |
|  |  |  |
| **11.** | **基于策略的无梯度算法** | **Policy-Based Gradient-Free Algorithms** |
| 11.1. | 无梯度算法 | Gradient-Free Algorithms |
| 11.1.1. | 进化策略算法 | ES: Evolution Strategy |
| 11.1.2. | 增强随机搜索 | ARS: Augmented Random Search |
| 11.2. | 无梯度算法和策略梯度算法比较 | Compare Gradient-Free Algorithms and Policy Gradient Algorithms |
| 11.3. | 案例：双足机器人 | Case Study: BipedalWalker |
| 11.3.1. | 奖励截断 | Reward Clipping |
| 11.3.2. | 用进化算法求解 | ES |
| 11.3.3. | 用增强随机搜索求解 | ARS |
| 11.4. | 本章小结 | Summary |
| 11.5. | 练习题 | Exercises |
|  |  |  |
| **12.** | **值分布强化学习** | **Distributional RL** |
| 12.1. | 价值分布及其性质 | Value Distribution and its Properties |
| 12.2. | 效用最大化强化学习 | Maximum Utility RL |
| 12.3. | 基于概率分布的算法 | Probability-based Algorithm |
| 12.3.1. | 类别深度Q网络算法 | C51: Categorical DQN |
| 12.3.2. | 带效用的类别深度Q网络算法 | Categorical DQN with Utility |
| 12.4. | 基于分位数的强化学习 | Quantile Based RL |
| 12.4.1. | 分位数回归深度Q网络算法 | QR-DQN: Quantile Regression Deep Q Network |
| 12.4.2. | 含蓄分位网络算法 | IQN: Implicit Quantile Networks |
| 12.4.3. | 带效用的分位数回归算法 | QR Algorithms with Utility |
| 12.5. | 类别深度Q网络算法与分位数回归算法的比较 | Compare Categorical DQN and QR Algorithms |
| 12.6. | 案例：Atari电动游戏Pong | Case Study: Atari Game Pong |
| 12.6.1. | Atari游戏环境的使用 | Atari Game Environment |
| 12.6.2. | Pong游戏 | The Game Pong |
| 12.6.3. | 包装Atari游戏环境 | Wrapper Class of Atari Environment |
| 12.6.4. | 用类别深度Q网络算法玩游戏 | Use Categorical DQN to Solve Pong |
| 12.6.5. | 用分位数回归深度Q网络算法玩游戏 | Use QR-DQN to Solve Pong |
| 12.6.6. | 用含蓄分位网络算法玩游戏 | Use IQN to Solve Pong |
| 12.7. | 本章小结 | Summary |
| 12.8. | 练习题 | Exercises |
|  |  |  |
| 13 | 最小化遗憾 | Minimize Regret |
| 13.1. | 遗憾 | Regret |
| 13.2. | 多臂赌博机 | MAB: Multi-Arm Bandit |
| 13.2.1. | 多臂赌博机问题描述 | MAB Problem |
| 13.2.2. | $\varepsilon$ 贪心算法 | $\varepsilon$ -Greedy Algorithm |
| 13.2.3. | 置信上界 | UCB: Upper Confidence Bound |
| 13.2.4. | Bayesian置信上界算法 | Bayesian UCB |
| 13.2.5. | Thompson采样算法 | Thompson Sampling |
| 13.3. | 置信上界价值迭代 | UCBVI: Upper Confidence Bound Value Iteration |
| 13.4. | 案例：Bernoulli奖励多臂赌博机 | Case Study: Bernoulli Reward MAB |
| 13.4.1. | 创建自定义环境 | Create Customed Environment |
| 13.4.2. | 用TODO 贪心策略求解 |  -Greedy Solver |
| 13.4.3. | 用第一置信上界求解 | UCB1 Solver |
| 13.4.4. | 用Bayesian置信上界求解 | Bayesian UCB Solver |
| 13.4.5. | 用Thompson采样求解 | Thompson Sampling Solver |
| 13.5. | 本章小结 | Summary |
| 13.6. | 练习题 | Exercises |
|  |  |  |
| **14.** | **树搜索** | **Tree Search** |
| 14.1. | 回合更新树搜索 | MCTS: Monte Carlo Tree Search |
| 14.1.1. | 选择 | Select |
| 14.1.2. | 扩展和评估 | Expand and Evaluate |
| 14.1.3. | 回溯 | Backup |
| 14.1.4. | 决策 | Decide |
| 14.1.5. | 训练回合更新树搜索用到的神经网络 | Train Networks in MCTS |
| 14.2. | 在棋盘游戏中的应用 | Application in Board Game |
| 14.2.1. | 棋盘游戏 | Board Games |
| 14.2.2. | 自我对弈 | Self-Play |
| 14.2.3. | 针对棋盘游戏的网络 | Neural Networks for Board Games |
| 14.2.4. | 从AlphaGo到MuZero | From AlphaGo to MuZero |
| 14.3. | 案例：井字棋 | Case Study: Tic-Tac-Toe |
| 14.3.1. | 棋盘游戏环境boardgame2 | boardgame2: Board Game Environment |
| 14.3.2. | 穷尽式搜索 | Exhaustive Search |
| 14.3.3. | 启发式搜索 | Heuristic Search |
| 14.4. | 本章小结 | Summary |
| 14.5. | 练习题 | Exercises |
|  |  |  |
| **15.** | **模仿学习和人类反馈强化学习** | **IL and RLHF: Imitation Learning and RL with Human Feedback** |
| 15.1. | 模仿学习 | IL: Imitation Learning |
| 15.1.1. | $f$ 散度及其性质 | $f$ -Divergences and their Properties |
| 15.1.2. | 行为克隆 | BC: Behavior Cloning |
| 15.1.3. | 生成对抗模仿学习 | GAIL: Generative Adversarial Imitation Learning |
| 15.2. | 人类反馈强化学习和生成性与训练变换模型 | RLHF and GPT |
| 15.3. | 案例：机器人行走 | Case Study: Humanoid |
| 15.3.1. | 扩展库PyBullet | The Library PyBullet |
| 15.3.2. | 用行为克隆模仿学习 | Use BC to IL |
| 15.3.3. | 用生成对抗模仿学习 | Use GAIL to IL |
| 15.4. | 本章小结 | Summary |
| 15.5. | 练习题 | Exercises |
|  |  |  |
| **16.** | **更多智能体/环境接口模型** | **More Agent–Environment Interfaces** |
| 16.1. | 平均奖励离散时间Markov决策过程 | Average Reward DTMDP |
| 16.1.1. | 平均奖励 | Average Reward |
| 16.1.2. | 差分价值 | Differential Values |
| 16.1.3. | 最优策略 | Optimal Policy |
| 16.2. | 连续时间Markov决策过程 | CTMDP: Continuous-Time MDP |
| 16.3. | 非齐次Markov决策过程 | Non-Stationary MDP |
| 16.3.1. | 非齐次状态表示 | Representation of Non-Stationary States |
| 16.3.2. | 时间指标有界的情况 | Bounded Time Index |
| 16.3.3. | 时间指标无界的情况 | Unbounded Time Index |
| 16.4. | 半Markov决策过程 | SMDP: Semi-MDP |
| 16.4.1. | 半Markov决策过程及其价值 | SMDP and its Values |
| 16.4.2. | 最优策略求解 | Find Optimal Policy |
| 16.4.3. | 分层强化学习 | HRL: Hierarchical Reinforcement Learning |
| 16.5. | 部分可观测Markov决策过程 | POMDP: Partially Observable Markov Decision Process |
| 16.5.1. | 离散时间部分可观测Markov决策过程 | DTPOMDP: Discrete-Time POMDP |
| 16.5.2. | 信念 | Belief |
| 16.5.3. | 信念Markov决策过程 | Belief MDP |
| 16.5.4. | 信念价值 | Belief Values |
| 16.5.5. | 有限部分可观测Markov决策过程的信念价值 | Belief Values for Finite POMDP |
| 16.5.6. | 使用记忆 | Use Memory |
| 16.6. | 案例：老虎 | Case Study: Tiger |
| 16.6.1. | 带折扣回报期望与平均奖励的比较 | Compare Discounted Return Expectation and Average Reward |
| 16.6.2. | 信念Markov决策过程 | Belief MDP |
| 16.6.3. | 非齐次的信念状态价值 | Non-Stationary Belief State Values |
| 16.7. | 本章小结 | Summary |
| 16.8. | 练习题 | Exercises |