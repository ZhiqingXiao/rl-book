# Table of Contents

## 1. Introduction of Reinforcement Learning (RL)

#### 1.1. What is RL?

#### 1.2. Applications of RL

#### 1.3. Agent–Environment Interface

#### 1.4. Taxonomy of RL

1.4.1. Task-Based Taxonomy

1.4.2. Algorithm-based Taxonomy

#### 1.5. Performance Metrics

#### 1.6. Case Study: Agent–Environment Interface in Gym

1.6.1. Install Gym

1.6.2. Use Gym

1.6.3. Example: MountainCar

#### 1.7. Summary

#### 1.8. Exercises

1.8.1. Multiple Choices

1.8.2. Programming

1.8.3. Mock Interview

## 2. MDP: Markov Decision Process

#### 2.1. MDP Model

2.1.1. DTMDP: Discrete-Time MDP

2.1.2. Environment and Dynamics

2.1.3. Policy

2.1.4. Discounted Return

#### 2.2. Value

2.2.1. Definition of Value

2.2.2. Properties of Values

2.2.3. Calculate Values

2.2.4. Calculate Initial Expected Return using Values

2.2.3. Partial Order of Policy and Policy Improvement

#### 2.3. Visitation Frequency

2.3.1. Definition of Visitation Frequency

2.3.2. Properties of Visitation Frequency

2.3.3. Calculate Visitation Frequency

2.3.4. Equivalence between Discounted Visitation Frequency and Policy

2.3.5. Expectation over Discounted Distribution

#### 2.4. Optimal Policy and Optimal Value

2.4.1. From Optimal Policy to Optimal Value

2.4.2. Existence of Optimal Policy

2.4.3. Properties of Optimal Values

2.4.4. Calculate Optimal Values

2.4.5. Use Optimal Values to Find Optimal Strategy

#### 2.5. Case Study: CliffWalking

2.5.1. Use Environment

2.5.2. Policy Evaluation

2.5.3. Solve Optimal Values

2.5.4. Solve Optimal Policy

#### 2.6. Summary

#### 2.7. Exercises

2.7.1. Multiple Choices

2.7.2. Programming

2.7.3. Mock Interview

## 3. Model-Based Numerical Iteration

#### 3.1. Bellman Operators and Its Properties

#### 3.2. Model-Based Policy Iteration

3.2.1. Policy Evaluation

3.2.2. Policy Improvement

3.2.3. Policy Iteration

#### 3.3. VI: Value Iteration

#### 3.4. Bootstrapping and Dynamic Programming

#### 3.5. Case Study: FrozenLake

3.5.1. Use Environment

3.5.2. Model-Based Policy Iteration

3.5.3. Model-Based VI

#### 3.6. Summary

#### 3.7. Exercises

3.7.1. Multiple Choices

3.7.2. Programming

3.7.3. Mock Interview

## 4. MC: Monte Carlo Learning

#### 4.1. On-Policy MC Learning

4.1.1. On-Policy MC Policy Evaluation

4.1.2. MC Learning with Exploration Start

4.1.3. MC Learning on Soft Policy

#### 4.2. Off-Policy MC Learning

4.2.1. Importance Sampling

4.2.2. Off-Policy MC Policy Evaluation

4.2.3. Off-Policy MC Policy Optimization

#### 4.3. Case Study: Blackjack

4.3.1. Use Environment

4.3.2. On-Policy Policy Evaluation

4.3.3. On-Policy Policy Optimization

4.3.4. Off-Policy Policy Evaluation

4.3.5. Off-Policy Policy Optimization

#### 4.4. Summary

#### 4.5. Exercises

4.5.1. Multiple Choices

4.5.2. Programming

4.5.3. Mock Interview

## 5. TD: Temporal Difference Learning

#### 5.1. TD return

#### 5.2. On-Policy TD Learning

5.2.1. TD Policy Evaluation

5.2.2. SARSA

5.2.3. Expected SARSA

#### 5.3. Off-Policy TD Learning

5.3.1. Off-Policy Algorithm based on Importance Sampling

5.3.2. Q Learning

5.3.3. Double Q Learning

#### 5.4. Eligibility Trace

5.4.1. $\lambda$ Return

5.4.2. TD $(\lambda)$

#### 5.5. Case Study: Taxi

5.5.1. Use Environment

5.5.2. On-Policy TD

5.5.3. Off-Policy TD

5.5.4. Eligibility Trace

#### 5.6. Summary

#### 5.7. Exercises

5.7.1. Multiple Choices

5.7.2. Programming

5.7.3. Mock Interview

## 6. Function Approximation

#### 6.1. Basic of Function Approximation

#### 6.2. Parameter Update using Gradient

6.2.1. SGD: Stochastic Gradient Descent

6.2.2. Semi-Gradient Descent

6.2.3. Semi-Gradient Descent with Eligibility Trace

#### 6.3. Convergence of Function Approximation

6.3.1. Condition of Convergence

6.3.2. Baird's Counterexample

#### 6.4. DQN: Deep Q Network

6.4.1. Experience Replay

6.4.2. Deep Q Learning with Target Network

6.4.3. Double DQN

6.4.4. Dueling DQN

#### 6.5. Case Study: MountainCar

6.5.1. Use Environment

6.5.2. Linear Approximation

6.5.3. DQN and its Variants

#### 6.6. Summary

#### 6.7. Exercises

6.7.1. Multiple Choices

6.7.2. Programming

6.7.3. Mock Interview

## 7. PG: Policy Gradient

#### 7.1. Theory of PG

7.1.1. Function Approximation for Policy

7.1.2. PG Theorem

7.1.3. Relationship between PG and Maximum Likelihood Estimate

#### 7.2. On-Policy PG

7.2.1. VPG: Vanilla Policy Gradient

7.2.2. PG with Baseline

#### 7.3. Off-Policy PG

#### 7.4. Case Study: CartPole

7.4.1. On-Policy PG

7.4.2. Off-Policy PG

#### 7.5. Summary

#### 7.6. Exercises

7.6.1. Multiple Choices

7.6.2. Programming

7.6.3. Mock Interview

## 8. AC: Actor–Critic

#### 8.1. Intuition of AC

#### 8.2. On-Policy AC

8.2.1. Action-Value AC

8.2.2. Advantage AC

8.2.3. Eligibility Trace AC

#### 8.3. On-Policy AC with Surrogate Objective

8.3.1. Performance Difference Lemma

8.3.2. Surrogate Advantage

8.3.3. PPO: Proximal Policy Optimization

#### 8.4. Natural PG and Trust Region Algorithm

8.4.1. Kullback–Leibler Divergence and Fisher Information Matrix

8.4.2. Trust Region of Surrogate Objective

8.4.3. NPG: Natural Policy Gradient

8.4.4. TRPO: Trust Region Policy Optimization

#### 8.5. Importance Sampling Off-Policy AC

#### 8.6. Case Study: Acrobot

8.6.1. On-Policy AC

8.6.2. On-Policy AC with Surrogate Objective

8.6.3. NPG and TRPO

8.6.4. Importance Sampling Off-Policy PG

#### 8.7. Summary

#### 8.8. Exercises

8.8.1. Multiple Choices

8.8.2. Programming

8.8.3. Mock Interview

## 9. DPG: Deterministic Policy Gradient

#### 9.1. DPG Theorem

#### 9.2. On-Policy DPG

#### 9.3. Off-Policy DPG

9.3.1. OPDAC: Off-Policy Deterministic Actor–Critic

9.3.2. DDPG: Deep Deterministic Policy Gradient

9.3.3. TD3: Twin Delay Deep Deterministic Policy Gradient

#### 9.4. Exploration Process

#### 9.5. Case Study: Pendulum

9.5.1. DDPG

9.5.2. TD3

#### 9.6. Summary

#### 9.7. Exercises

9.7.1. Multiple Choices

9.7.2. Programming

9.7.3. Mock Interview

## 10. Maximum-Entropy RL

#### 10.1. Maximum-Entropy RL and Soft RL

10.1.1. Reward Engineering and Reward with Entropy

10.1.2. Soft Values

10.1.3. Soft Policy Improvement Theorem and Numeric Iterative Algorithm

10.1.4. Optimal Values

10.1.5. Soft Policy Gradient Theorem

#### 10.2. Soft RL Algorithms

10.2.1. SQL: Soft Q Learning

10.2.2. SAC: Soft Actor–Critic

#### 10.3. Automatic Entropy Adjustment

#### 10.4. Case Study: Lunar Lander

10.4.1. Install Environment

10.4.2. Use Environment

10.4.3. Use SQL to Solve LunarLander

10.4.4. Use SAC to Solve LunarLander

10.4.5. Use Automatic Entropy Adjustment to Solve LunarLander

10.4.6. Solve LunarLanderContinuous

#### 10.5. Summary

#### 10.6. Exercises

10.6.1. Multiple Choices

10.6.2. Programming

10.6.3. Mock Interview

## 11. Policy-Based Gradient-Free Algorithms

#### 11.1. Gradient-Free Algorithms

11.1.1. ES: Evolution Strategy

11.1.2. ARS: Augmented Random Search

#### 11.2. Compare Gradient-Free Algorithms and Policy Gradient Algorithms

#### 11.3. Case Study: BipedalWalker

11.3.1. Reward Clipping

11.3.2. ES

11.3.3. ARS

#### 11.4. Summary

#### 11.5. Exercises

11.5.1. Multiple Choices

11.5.2. Programming

11.5.3. Mock Interview

## 12. Distributional RL

#### 12.1. Value Distribution and its Properties

#### 12.2. Maximum Utility RL

#### 12.3. Probability-Based Algorithm

12.3.1. C51: Categorical DQN

12.3.2. Categorical DQN with Utility

#### 12.4. Quantile Based RL

12.4.1. QR-DQN: Quantile Regression Deep Q Network

12.4.2. IQN: Implicit Quantile Networks

12.4.3. QR Algorithms with Utility

#### 12.5. Compare Categorical DQN and QR Algorithms

#### 12.6. Case Study: Atari Game Pong

12.6.1. Atari Game Environment

12.6.2. The Game Pong

12.6.3. Wrapper Class of Atari Environment

12.6.4. Use Categorical DQN to Solve Pong

12.6.5. Use QR-DQN to Solve Pong

12.6.6. Use IQN to Solve Pong

#### 12.7. Summary

#### 12.8. Exercises

12.8.1. Multiple Choices

12.8.2. Programming

12.8.3. Mock Interview

## 13. Minimize Regret

####  13.1. Regret

#### 13.2. MAB: Multi-Arm Bandit

13.2.1. MAB Problem

13.2.2. $\varepsilon$-Greedy Algorithm

13.2.3. UCB: Upper Confidence Bound

13.2.4. Bayesian UCB

13.2.5. Thompson Sampling

#### 13.3. UCBVI: Upper Confidence Bound Value Iteration

#### 13.4. Case Study: Bernoulli Reward MAB

13.4.1. Create Customed Environment

13.4.2. $\varepsilon$-Greedy Solver

13.4.3. UCB1 Solver

13.4.4. Bayesian UCB Solver

13.4.5. Thompson Sampling Solver

#### 13.5. Summary

#### 13.6. Exercises

13.6.1. Multiple Choices

13.6.2. Programming

13.6.3. Mock Interview

## 14. Tree Search

#### 14.1. MCTS: Monte Carlo Tree Search

14.1.1. Select

14.1.2. Expand and Evaluate

14.1.3. Backup

14.1.4. Decide

14.1.5. Train Networks in MCTS

#### 14.2. Application in Board Game

14.2.1. Board Games

14.2.2. Self-Play

14.2.3. Neural Networks for Board Games

14.2.4. From AlphaGo to MuZero

#### 14.3. Case Study: Tic-Tac-Toe

14.3.1. boardgame2: Board Game Environment

14.3.2. Exhaustive Search

14.3.3. Heuristic Search

#### 14.4. Summary

#### 14.5. Exercises

14.5.1. Multiple Choices

14.5.2. Programming

14.5.3. Mock Interview

## 15. More Agent–Environment Interfaces

#### 15.1. Average Reward DTMDP

15.1.1. Average Reward

15.1.2. Differential Values

15.1.3. Optimal Policy

#### 15.2. CTMDP: Continuous-Time MDP

#### 15.3. Non-Stationary MDP

15.3.1. Representation of Non-Stationary States

15.3.2. Bounded Time Index

15.3.3. Unbounded Time Index

#### 15.4. SMDP: Semi-MDP

15.4.1. SMDP and its Values

15.4.2. Find Optimal Policy

15.4.3. HRL: Hierarchical Reinforcement Learning

#### 15.5. POMDP: Partially Observable Markov Decision Process

15.5.1. DTPOMDP: Discrete-Time POMDP

15.5.2. Belief

15.5.3. Belief MDP

15.5.4. Belief Values

15.5.5. Belief Values for Finite POMDP

15.5.6. Use Memory

#### 15.6. Case Study: Tiger

15.6.1. Compare Discounted Return Expectation and Average Reward

15.6.2. Belief MDP

15.6.3. Non-Stationary Belief State Values

#### 15.7. Summary

#### 15.8. Exercises

15.8.1. Multiple Choices

15.8.2. Programming

15.8.3. Mock Interview

## 16. Learning from Feedback and Imitation Learning

#### 16.1 Learning from Feedback

16.1.1. Reward Model

16.1.2. PbRL: Preference-based RL

16.1.3. RLHF: Reinforcement Learning with Human Feedback

#### 16.2 IL: Imitation Learning

16.2.1. $f$-Divergences and their Properties

16.2.2. BC: Behavior Cloning

16.2.3. GAIL: Generative Adversarial Imitation Learning

#### 16.3 Application in Training GPT

#### 16.4. Case Study: Humanoid

16.4.1. Use PyBullet

16.4.2. Use BC to IL

16.4.3. Use GAIL to IL

#### 16.5. Summary

#### 16.6. Exercises

16.6.1. Multiple Choices

16.6.2. Programming

16.6.3. Mock Interview
