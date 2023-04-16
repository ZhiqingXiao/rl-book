## 2.3. Discounted Visitation Frequency

The previous section covers values, a very important concept in RL. This section will cover another import concept called discounted visitation frequency, also known as discounted distribution, which is a dual quantity of values. Based on the discounted distribution, we can further define discounted expectations. They all play important roles in RL researches.

### 2.3.1. Definition of Discounted Visitation Frequency

Given the environment and the policy of an MDP, we can determine how many times a state or a state每action pair will be visited. Taking possible discounts into considerations, we can define a statistic called discounted visitation frequency, which is also known as discounted distribution. It has two forms:

- **Discounted state visitation frequency** (also known as discounted state distribution)

$$
\begin{array}{l}
{\text{episodic task:}} & {\rho _\pi }\left( \mathsfit{s} \right) = \sum\limits_{t = 1}^{ + \infty } {{{\Pr }_\pi }\left[ {T = t} \right]\sum\limits_{\tau  = 0}^{t - 1} {{\gamma ^\tau }{{\Pr }_\pi }\left[ {{\mathsfit{S}_\tau } = \mathsfit{s}} \right]} } , & \mathsfit{s} \in \mathcal{S};\\
{\text{sequential task:}} & {\rho _\pi }\left( \mathsfit{s} \right) = \sum\limits_{\tau  = 0}^{ + \infty } {{\gamma ^\tau }{{\Pr }_\pi }\left[ {{\mathsfit{S}_\tau } = \mathsfit{s}} \right]} , & \mathsfit{s} \in \mathcal{S}.
\end{array}
$$

- **Discounted state每action visitation frequency** (also known as discounted state每action distribution)

$$\begin{array}{l}
{\text{episodic task:}} & {\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right) = \sum\limits_{t = 1}^{ + \infty } {{{\Pr }_\pi }\left[ {T = t} \right]\sum\limits_{\tau  = 0}^{t - 1} {{\gamma ^\tau }{{\Pr }_\pi }\left[ {{\mathsfit{S}_\tau } = \mathsfit{s},{\mathsfit{A}_\tau } = \mathsfit{a}} \right]} } , & \mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}\left( \mathsfit{s} \right);\\
{\text{sequential task:}} & {\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right) = \sum\limits_{t = 0}^{ + \infty } {{\gamma ^\tau }{{\Pr }_\pi }\left[ {{\mathsfit{S}_\tau } = \mathsfit{s},{\mathsfit{A}_\tau } = \mathsfit{a}} \right]} , & \mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}\left( \mathsfit{s} \right).
\end{array}
$$

 
***Note:***
Although discounted visitation is also called discounted distribution, it may not be a probability distribution. We can verify that,

$$
\begin{array}{l}
{\text{episodic task:}} & \sum\limits_{\mathsfit{s} \in \mathcal{S}} {{\rho _\pi }\left( \mathsfit{s} \right)}  = \sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}\left( \mathsfit{s} \right)} {{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)}  = {{\mathrm{E}}_\pi }\left[ {\frac{{1 - {\gamma ^T}}}{{1 - \gamma }}} \right];\\
{\text{sequential task:}} & \sum\limits_{\mathsfit{s} \in \mathcal{S}} {{\rho _\pi }\left( \mathsfit{s} \right)}  = \sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}\left( \mathsfit{s} \right)} {{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)}  = \frac{1}{{1 - \gamma }}.
\end{array}
$$

Proof for the episodic tasks:

$$
\begin{array}{l}
\sum\limits_{\mathsfit{s} \in \mathcal{S}} {{\rho _\pi }\left( \mathsfit{s} \right)}  &  = \sum\limits_{\mathsfit{s} \in \mathcal{S}} {\sum\limits_{t = 1}^{ + \infty } {{{\Pr }_\pi }\left[ {T = t} \right]\sum\limits_{\tau  = 0}^{t - 1} {{\gamma ^\tau }{{\Pr }_\pi }\left[ {{\mathsfit{S}_\tau } = \mathsfit{s}} \right]} } } \\
 &  = \sum\limits_{t = 1}^{ + \infty } {{{\Pr }_\pi }\left[ {T = t} \right]\sum\limits_{\tau  = 0}^{t - 1} {{\gamma ^\tau }\sum\limits_{\mathsfit{s} \in \mathcal{S}} {{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s}} \right]} } } \\
 &  = \sum\limits_{t = 1}^{ + \infty } {{{\Pr }_\pi }\left[ {T = t} \right]\sum\limits_{\tau  = 0}^{t - 1} {{\gamma ^\tau }} } \\
 &  = \sum\limits_{t = 1}^{ + \infty } {{{\Pr }_\pi }\left[ {T = t} \right]\frac{{1 - {\gamma ^t}}}{{1 - \gamma }}} \\
 &  = {{\mathrm{E}}_\pi }\left[ {\frac{{1 - {\gamma ^T}}}{{1 - \gamma }}} \right].
\end{array}
$$

Apparently, this expectation does not always equal 1. Therefore, the discounted distribution is not always a distribution.

Rewards do not appear in the definition of discounted visitation frequency. Therefore, discounted visitation frequencies do not directly depend on rewards.

### 2.3.2. Properties of Discounted Visitation Frequency

Discounted state visitation frequency and discounted state每action visitation frequency have the following relationships.

- Use discounted state visitation frequency and policy to back up discounted state每action visitation frequency

$$
{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right) = {\rho _\pi }\left( \mathsfit{s} \right)\pi \left( {\mathsfit{a}|\mathsfit{s}} \right),
\kern1em
\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}\left( \mathsfit{s} \right).
$$


(Proof: Taking sequential task as an example,

$$
{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right) = \sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s},{\mathsfit{A}_t} = \mathsfit{a}} \right]}  = \sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s}} \right]\pi \left( {\mathsfit{a}|\mathsfit{s}} \right)}  = {\rho _\pi }\left( \mathsfit{s} \right)\pi \left( {\mathsfit{a}|\mathsfit{s}} \right)
$$


We can prove for episodic tasks in a similar way.)

- Use discounted state每action visitation frequency to back up discounted state visitation frequency

$$
{\rho _\pi }\left( \mathsfit{s} \right) = \sum\limits_{\mathsfit{a} \in {{\cal A}}\left( \mathsfit{s} \right)} {{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)},
\kern1em
\mathsfit{s} \in \mathcal{S}.
$$


(Proof: For sequential tasks,

$$
\begin{array}{l}
 & {\rho _\pi }\left( \mathsfit{s} \right) &  = \sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s}} \right]} \\
 & \quad  &  = \sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}\sum\limits_{\mathsfit{a} \in {{\cal A}}\left( \mathsfit{s} \right)} {{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s},{\mathsfit{A}_t} = \mathsfit{a}} \right]} } \\
 & \quad  &  = \sum\limits_{\mathsfit{a} \in {{\cal A}}\left( \mathsfit{s} \right)} {\sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s},{\mathsfit{A}_t} = \mathsfit{a}} \right]} } \\
 & \quad  &  = \sum\limits_{\mathsfit{a} \in {{\cal A}}\left( \mathsfit{s} \right)} {{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)} .
\end{array}
$$


We can prove for sequential tasks in a similar way.)

- Use discounted state每action visitation frequency and dynamics to back up discounted state visitation frequency.

$$
{\rho _\pi }\left( {\mathsfit{s'}} \right) = {p_{{\mathsfit{S}_0}}}\left( {\mathsfit{s'}} \right) + \sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}\left( \mathsfit{s} \right)} {\gamma p\left( {\mathsfit{s'}|\mathsfit{s},\mathsfit{a}} \right){\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)},
\kern1em
\mathsfit{s'} \in \mathcal{S}
$$

(Proof: For sequential tasks, taken the definition of ${\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)$ for examples, we have

$$
\begin{array}{l}
\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right)}{\gamma p\left(\mathsfit{s'}\mid\mathsfit{s},\mathsfit{a}\right){\rho _\pi }\left(\mathsfit{s},\mathsfit{a}\right)}
\\
\quad=
\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right)}{\gamma p\left(\mathsfit{s'}\mid\mathsfit{s},\mathsfit{a}\right)\sum\limits_{t=0}^{+\infty}{\gamma^t{\Pr}_\pi\left[\mathsfit{S}_t=\mathsfit{s},\mathsfit{A}_t=\mathsfit{a}\right]}}
\\
\quad=
\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right)}{\gamma p\left(\mathsfit{s'}\mid\mathsfit{s},\mathsfit{a}\right)\sum\limits_{\mathsfit{s}_0\in\mathcal{S}}{p_{\mathsfit{S}_0}}\left(\mathsfit{s}_0\right)\sum\limits_{t=1}^{+\infty} {\gamma^t{\Pr}_\pi\left[{\mathsfit{S}_t=\mathsfit{s},\mathsfit{A}_t=\mathsfit{a}\mid\mathsfit{S}_0=\mathsfit{s}_0} \right]}}
\end{array}
$$

$$
\begin{array}{l}
\quad=
\sum\limits_{\mathsfit{s}_0 \in\mathcal{S}}{p_{\mathsfit{S}_0}\left(\mathsfit{s}_0\right)\sum\limits_{t=1}^{+\infty}{\gamma^{t+1}\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right)}{p\left(\mathsfit{s'}\mid\mathsfit{s},\mathsfit{a}\right){\Pr}_\pi\left[\mathsfit{S}_t=\mathsfit{s},\mathsfit{A}_t= \mathsfit{a}\mid\mathsfit{S}_0=\mathsfit{s}_0\right]}}}
\\
\quad=
\sum\limits_{\mathsfit{s}_0 \in\mathcal{S}}{p_{\mathsfit{S}_0}\left(\mathsfit{s}_0\right)\sum\limits_{t=1}^{+\infty}{\gamma^{t+1}\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left( \mathsfit{s}\right)}{{\Pr}_\pi\left[ \mathsfit{S}_{t+1}=\mathsfit{s'},\mathsfit{S}_t=\mathsfit{s},\mathsfit{A}_t=\mathsfit{a}\mid\mathsfit{S}_0=\mathsfit{s}_0\right]}}}
\\
\quad=
\sum\limits_{\mathsfit{s}_0 \in\mathcal{S}}{p_{\mathsfit{S}_0}\left(\mathsfit{s}_0\right)\sum\limits_{t=1}^{+\infty}{\gamma^{t+1}{\Pr}_\pi\left[\mathsfit{S}_{t+1}=\mathsfit{s'}\mid\mathsfit{S}_0=\mathsfit{s}_0\right]}}.
\end{array}
$$

Let ${1_{\left[  \cdot  \right]}}$ be the indicator function. We have

$$
\begin{array}{l}
\sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right]} \\
\quad  = {\Pr _\pi }\left[ {{\mathsfit{S}_0} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right] + \sum\limits_{t = 1}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right]} \\
\quad  = {1_{\left[ {\mathsfit{s'} = {\mathsfit{s}_0}} \right]}} + \sum\limits_{t = 0}^{ + \infty } {{\gamma ^{t + 1}}{{\Pr }_\pi }\left[ {{\mathsfit{S}_{t + 1}} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right]} 
\end{array}
$$


So

$$
\sum\limits_{t = 0}^{ + \infty } {{\gamma ^{t + 1}}{{\Pr }_\pi }\left[ {{\mathsfit{S}_{t + 1}} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right]}  = \left( {\sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right]} } \right) - {1_{\left[ {\mathsfit{s'} = {\mathsfit{s}_0}} \right]}}.
$$


Plugging in the aforementioned equation into the equation in the beginning of the proof, we have

$$
\begin{array}{l}
\sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}\left( \mathsfit{s} \right)} {\gamma p\left( {\mathsfit{s'}|\mathsfit{s},\mathsfit{a}} \right){\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)} \\
\quad  = \sum\limits_{{\mathsfit{s}_0} \in {\mathcal{S}}} {{p_{{\mathsfit{S}_0}}}\left( {{\mathsfit{s}_0}} \right)\left( {\sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right]}  - {1_{\left[ {\mathsfit{s'} = {\mathsfit{s}_0}} \right]}}} \right)} \\
\quad  = \sum\limits_{{\mathsfit{s}_0} \in {\mathcal{S}}} {{p_{{\mathsfit{S}_0}}}\left( {{\mathsfit{s}_0}} \right)\sum\limits_{t = 0}^{ + \infty } {{\gamma ^t}{{\Pr }_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s'|}{\mathsfit{S}_0} = {\mathsfit{s}_0}} \right]} }  - {p_{{\mathsfit{S}_0}}}\left( {\mathsfit{s'}} \right)\\
\quad  = {\rho _\pi }\left( {\mathsfit{s'}} \right) - {p_{{\mathsfit{S}_0}}}\left( {\mathsfit{s'}} \right).
\end{array}
$$


The proof completes.)


The Bellman expectation equations among discounted visitation frequencies are as follows:

- Use the state distribution at time $t$ to back up the state distribution at time $t+1$:

$$
{\rho _\pi }\left( \mathsfit{s} \right) = {p_{{\mathsfit{S}_0}}}\left( \mathsfit{s} \right) + \sum\limits_{\mathsfit{s'} \in \mathcal{S}} {\gamma {p_\pi }\left( {\mathsfit{s}|\mathsfit{s'}} \right){\rho _\pi }\left( {\mathsfit{s'}} \right)} ,\quad \mathsfit{s'} \in \mathcal{S}
$$


(Proof: Plug

$${\rho _\pi }\left( {\mathsfit{s'},\mathsfit{a'}} \right) = {\rho _\pi }\left( {\mathsfit{s'}} \right)\pi \left( {\mathsfit{a'}|\mathsfit{s'}} \right),
\quad
\mathsfit{s'}\in\mathcal{S},\mathsfit{a'}\in{\cal A}\left(\mathsfit{s'}\right)
$$

into

$$
{\rho _\pi }\left( \mathsfit{s} \right) = {p_{{\mathsfit{S}_0}}}\left( \mathsfit{s} \right) + \sum\limits_{\mathsfit{s'} \in \mathcal{S},\mathsfit{a'} \in {\cal A}\left( \mathsfit{s} \right)} {\gamma p\left( {\mathsfit{s}|\mathsfit{s'},\mathsfit{a'}} \right){\rho _\pi }\left( {\mathsfit{s'},\mathsfit{a'}} \right)},
\quad
\mathsfit{s'}\in\mathcal{S},
$$

and simplify using

$$
p_\pi\left(\mathsfit{s}\mid\mathsfit{s'}\right)=\sum\limits_{\mathsfit{a'}} {p\left( \mathsfit{s}\mid\mathsfit{s'},\mathsfit{a'}\right)\pi\left(\mathsfit{a'}\mid\mathsfit{s'}\right)} ,
\quad
\mathsfit{s} \in \mathcal{S},\mathsfit{s'} \in \mathcal{S}
$$

The proof completes.)

- Use state每action distribution at time $t$ to back up the state每action distribution at time $t+1$:

$$
\rho_\pi\left(\mathsfit{s},\mathsfit{a}\right)=p_{0,\pi}\left(\mathsfit{s},\mathsfit{a}\right)+\sum\limits_{\mathsfit{s'}\in \mathcal{S}} {\gamma {p_\pi }\left(\mathsfit{s},\mathsfit{a}\mid\mathsfit{s'},\mathsfit{a'}\right){\rho_\pi}\left( {\mathsfit{s'},\mathsfit{a'}} \right)} ,\quad \mathsfit{s}\in\mathcal{S},\mathsfit{a}\in{\cal A}\left(\mathsfit{s}\right),
$$

where

$$
{p_{0,\pi}}\left(\mathsfit{s},\mathsfit{a}\right)=\pi\left(\mathsfit{a}\mid\mathsfit{s}\right){p_{\mathsfit{S}_0}}\left(\mathsfit{s}\right),\quad\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in {\cal A}\left(\mathsfit{s}\right).
$$

(Proof: Multiply both sides of

$$
{\rho_\pi}\left(\mathsfit{s}\right) = {p_{\mathsfit{S}_0}}\left(\mathsfit{s}\right)+\sum\limits_{\mathsfit{s'}\in\mathcal{S},\mathsfit{a'}\in{\cal A}\left(\mathsfit{s}\right)}{\gamma p\left(\mathsfit{s}\mid\mathsfit{s'},\mathsfit{a'}\right){\rho_\pi }\left(\mathsfit{s'},\mathsfit{a'}\right)} \quad \mathsfit{s}\in\mathcal{S}
$$

by $\pi\left(\mathsfit{a}\mid\mathsfit{s}\right)$, and simplify using

$$
\rho_\pi\left(\mathsfit{s},\mathsfit{a}\right)=\rho_\pi\left(\mathsfit{s}\right)\pi\left(\mathsfit{a}\mid\mathsfit{s}\right),
\quad
\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in{\cal A}\left(\mathsfit{s}\right)
$$

and

$$
p_\pi\left(\mathsfit{s},\mathsfit{a}\mid\mathsfit{s'},\mathsfit{a'}\right)=\pi\left(\mathsfit{a}\mid\mathsfit{s}\right)p\left( {\mathsfit{s}|\mathsfit{s'},\mathsfit{a'}} \right),
\quad
\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A},\mathsfit{s'}\in\mathcal{S},\mathsfit{a'}\in\mathcal{A}.
$$

The proof completes.)

Section 2.2.2 introduced the vector representation of Bellman expectation equations of values. The Bellman expectation equations among discounted visitation frequencies also have vector representation.

- Use the state distribution at time $t$ to back up the state distribution at time $t+1$:

$$
\boldsymbol\uprho_\pi=\mathbf{p}_{\mathsfit{S}_0}+\gamma\mathbf{P}_\pi\boldsymbol\uprho_\pi
$$

where the column vector

$$
{\mathbf{p}_{\mathsfit{S}_0}}={\left( {{p_{{\mathsfit{S}_0}}}\left(\mathsfit{s}\right):\mathsfit{s}\in\mathcal{S}} \right)^{\mathrm{T}}}
$$

has $\left|\mathcal{S}\right|$ elements, the column vector

$$
\boldsymbol\uprho_\pi=\left(\rho_\pi\left(\mathsfit{s}\right):\mathsfit{s}\in\mathcal{S}\right)^\mathrm{T}
$$

has $\left|\mathcal{S} \right|$ elements, and the matrix

$$
\mathbf{P}_\pi=\left(p_\pi\left(\mathsfit{s}\mid\mathsfit{s'}\right):\mathsfit{s} \in \mathcal{S},\mathsfit{s'}\in\mathcal{S}\right)
$$

has $\left|\mathcal{S}\right|\times \left|\mathcal{S}\right|$ elements.

- Use state每action distribution at time $t$ to back up the state每action distribution at time $t+1$:

$$
\boldsymbol\uprho_\pi=\mathbf{p}_0+\gamma\mathbf{P}_\pi\boldsymbol\uprho_\pi
$$

where the column vector

$$
\mathbf{p}_0=\left(\pi\left(\mathsfit{a}\mid\mathsfit{s}\right){p_{\mathsfit{S}_0}}\left( \mathsfit{s} \right):\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in{\cal A}\right)^{\mathrm{T}}
$$

has $\left|\mathcal{S}\right|\left|\mathcal{A} \right|$ elements, the column vector 

$$
\boldsymbol\uprho_\pi={\left( {{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right):\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in {\cal A}} \right)^{\mathrm{T}}}
$$

has $\left|\mathcal{S}\right|\left|\mathcal{A}\right|$ elements, and the matrix

$$
\mathbf{P}_\pi=\left(p_\pi\left(\mathsfit{s},\mathsfit{a}\mid\mathsfit{s'},\mathsfit{a'}\right):\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A},\mathsfit{s'}\in \mathcal{S},\mathsfit{a'}\in\mathcal{A}\right)
$$

has $\left|\mathcal{S}\right|\left| \mathcal{A}\right|\times\left|\mathcal{S}\right|\left|\mathcal{A}\right|$ elements.

### 2.3.3. Equivalence between Discounted Visitation Frequency and Policy

Section 2.3.2 told us that the discounted visitation frequencies of an arbitrary policy $\pi$ satisfy the following equation set:

$$
\begin{array}{l}
& {\rho _\pi }\left( {\mathsfit{s'}} \right) = {p_{{\mathsfit{S}_0}}}\left( {\mathsfit{s'}} \right) + \sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right)} {\gamma p\left( {\mathsfit{s'}|\mathsfit{s},\mathsfit{a}} \right){\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)} , & \mathsfit{s'} \in \mathcal{S}\\
& {\rho _\pi }\left( \mathsfit{s} \right) = \sum\limits_{\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right)} {{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)} , & \mathsfit{s} \in \mathcal{S}\\
& {\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right) \ge 0, & \mathsfit{s} \in \mathcal{S},\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right).
\end{array}
$$

Note that the equation set does not include $\pi$ explicitly. In fact, the solution of the above equation set is bijective with the policy. Exactly speaking, if a suite of $\rho\left(\mathsfit{s}\right)$ ( $\mathsfit{s}\in\mathcal{S}$ ) and $\rho\left(\mathsfit{s},\mathsfit{a}\right)$ ( $\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in \mathcal{A}\left(\mathsfit{s}\right)$ ) satisfies the above equation set, we use the solution of the equation set to define a policy

$$
\pi\left(\mathsfit{a}\mid\mathsfit{s}\right)=\frac{\rho\left(\mathsfit{s},\mathsfit{a}\right)}{\rho\left(\mathsfit{s}\right)}
$$

and the policy will satisfy (1) $\rho_\pi\left(\mathsfit{s}\right) = \rho \left( \mathsfit{s} \right)$ ( $\mathsfit{s} \in \mathcal{S}$ ); (2) $\rho_\pi\left(\mathsfit{s},\mathsfit{a}\right) = \rho \left(\mathsfit{s},\mathsfit{a}\right)$ ( $\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left( \mathsfit{s} \right)$ ). (Proof: Consider sequential tasks. (1) For any $\mathsfit{s'}\in\mathcal{S}$, taking the definition of policy $\pi$, we will know

$$
\begin{array}{l}
& \rho \left( {\mathsfit{s'}} \right) &  = {p_{{\mathsfit{S}_0}}}\left( {\mathsfit{s'}} \right) + \sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right)} {\gamma p\left( {\mathsfit{s'}|\mathsfit{s},\mathsfit{a}} \right)\rho \left( {\mathsfit{s},\mathsfit{a}} \right)} \\
& \quad  &  = {p_{{\mathsfit{S}_0}}}\left( {\mathsfit{s'}} \right) + \sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right)} {\gamma p\left( {\mathsfit{s'}|\mathsfit{s},\mathsfit{a}} \right)\rho \left( \mathsfit{s} \right)\pi \left( {\mathsfit{a}|\mathsfit{s}} \right)} \\
& \quad  &  = {p_{{\mathsfit{S}_0}}}\left( {\mathsfit{s'}} \right) + \sum\limits_{\mathsfit{s} \in \mathcal{S}} {\gamma {p_\pi }\left( {\mathsfit{s'}|\mathsfit{s}} \right)\rho \left( \mathsfit{s} \right)} .
\end{array}
$$


Therefore, $\rho\left(\mathsfit{s}\right)$ ( $\mathsfit{s}\in\mathcal{S}$ ) satisfies the Bellman expectation equation. Consider the vector form of Bellmen expectation equation. Rewrite $\rho\left(\mathsfit{s}\right)$ ( $\mathsfit{s}\in\mathcal{S}$ ) as $\boldsymbol\uprho$ , a vector of length $\left| \mathcal{S} \right|$. Rewrite the initial state distribution

$$
p_{\mathsfit{S}_0}\left(\mathsfit{s}\right),
\quad
\mathsfit{s}\in\mathcal{S}
$$

as $\mathbf{p}_{0}$, a vector of length $\left|\mathcal{S}\right|$. Rewrite state transition probability

$$
p_\pi\left(\mathsfit{s'}\mid\mathsfit{s}\right),
\quad
\mathsfit{s},\mathsfit{s'}\in \mathcal{S}
$$

as a single-step transition probability matrix $\mathbf{P}_\pi$, a matrix of size $\left|\mathcal{S}\right|\times\left|\mathcal{S}\right|$. Then the above equation can be re-written as

$$
\boldsymbol\uprho=\mathbf{p}_0+\gamma\mathbf{P}_\pi\boldsymbol\uprho.
$$

Furthermore,

$$
\boldsymbol\uprho=\left(\mathbf{I}-\gamma\mathbf{P}_\pi\right)^{-1}\mathbf{p}_0
,
$$

where $\mathbf{I}$ is the identity matrix. Noticing that

$$
\left(\mathbf{I}-\gamma\mathbf{P}_\pi\right)^{-1}=\sum\limits_{t=0}^{+\infty}{{{\left(\gamma \mathbf{P}_\pi\right)}^t}}=\sum\limits_{t=0}^{+\infty}{\gamma^t\mathbf{P}_\pi^t}
,
$$

we have

$$
\boldsymbol\uprho=\sum\limits_{t=0}^{+\infty}{\gamma^t\mathbf{P}_\pi^t}\mathbf{p}_0
,
$$

where $\mathbf{P}_\pi^t$ can be viewed as a multi-step transition probability matrix. Therefore, we have

$$
\rho \left( {\mathsfit{s'}} \right) = \sum\limits_{{\mathsfit{s}_0} \in \mathcal{S}} {{p_{{\mathsfit{S}_0}}}\left( \mathsfit{s} \right)\sum\limits_{t = 0}^{ + \infty } {\sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right)} {{\gamma ^t}{{\Pr}_\pi }\left[ {{\mathsfit{S}_t} = \mathsfit{s'}|{\mathsfit{S}_0} = \mathsfit{s}} \right]} } }  = {\rho _\pi }\left( {\mathsfit{s'}} \right)
$$

(2) For any $\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right)$, we have ${\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right) = {\rho _\pi }\left( \mathsfit{s} \right)\pi \left( {\mathsfit{a}|\mathsfit{s}} \right)$, and $\rho \left( {\mathsfit{s},\mathsfit{a}} \right) = \rho \left( \mathsfit{s} \right)\pi \left( {\mathsfit{a}|\mathsfit{s}} \right)$. Therefore, ${\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right) = \rho \left( {\mathsfit{s},\mathsfit{a}} \right)$.)

***Note:***
This proof uses the vector representation. Vector representation is usually to solve the form

$$
\mathbf{y}=\left(\mathbf{I}-\gamma\mathbf{P}_\pi\right){\mathbf{x}}
,
$$

where the relation

$$
{\left(\mathbf{I}-\gamma\mathbf{P}_\pi\right)^{-1}}=\sum\limits_{t=0}^{+\infty}{{\left(\gamma \mathbf{P}_\pi\right)}^t}=\sum\limits_{t=0}^{+\infty}{\gamma^t\mathbf{P}_\pi^t}
$$

is usually used at the same time.

### 2.3.4. Expectation over Discounted Distribution

Although discounted distribution is usually not a probability distribution, we can still define expectation over the discounted distribution. Mathematically speaking, given a deterministic function $f$, we can define the expectation over discounted distribution as


$$
\begin{array}{l}
 & {{\mathrm{E}}_{\mathsfit{S}\sim{\rho_\pi }}}\left[ {f\left( \mathsfit{S} \right)} \right] &  = \sum\limits_{\mathsfit{s} \in \mathcal{S}} {{\rho _\pi }\left( \mathsfit{s} \right)f\left( \mathsfit{s} \right)} \\
 & {{\mathrm{E}}_{\left( {\mathsfit{S},\mathsfit{A}} \right)\sim{\rho _\pi }}}\left[ {f\left( {\mathsfit{S},\mathsfit{A}} \right)} \right] &  = \sum\limits_{\mathsfit{s} \in \mathcal{S},\mathsfit{a} \in \mathcal{A}\left( \mathsfit{s} \right)} {{\rho _\pi }\left( {\mathsfit{s},\mathsfit{a}} \right)f\left( {\mathsfit{s},\mathsfit{a}} \right)} .
\end{array}
$$

Many statistics can be represented using the notation of expectation over discounted distribution.

***Example:*** The expectation of return can be represented as

$$
g_\pi= {\mathrm{E}_{\left(\mathsfit{S},\mathsfit{A}\right)\sim{\rho_\pi}}}\left[ {r\left( {\mathsfit{S},\mathsfit{A}} \right)} \right]
$$

(Proof:

$$
\begin{array}{l}
g_\pi
&=
\mathrm{E}_\pi\left[G_0\right]
\\
&=
\mathrm{E}_\pi\left[\sum\limits_{t=0}^{+\infty}{\gamma^t{R_{t+1}}}\right]
\\
&=
\sum\limits_{t=0}^{+\infty}{\gamma^t{\mathrm{E}_\pi}\left[ {{R_{t+1}}} \right]}
\\
&=
\sum\limits_{t=0}^{+\infty}{\gamma^t{\mathrm{E}_\pi}\left[ {\mathrm{E}_\pi\left[R_{t+1}\mid{\mathsfit{S}_t},{\mathsfit{A}_t}\right]} \right]}
&
\text{due to law of total probability}
\\
&=
\sum\limits_{t=0}^{+\infty}{\gamma^t{\mathrm{E}_\pi}\left[r\left( {\mathsfit{S}_t,\mathsfit{A}_t}\right)\right]}
&
\text{due to definition of }r\left(\mathsfit{S}_t,\mathsfit{A}_t\right)
\end{array}
$$

$$
\begin{array}{l}
&=
\sum\limits_{t=0}^{+\infty}{\gamma^t\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a} \in \mathcal{A}\left(\mathsfit{s}\right)}{{\Pr}_\pi\left[{\mathsfit{S}_t}=\mathsfit{s},{\mathsfit{A}_t}=\mathsfit{a}\right]r\left(\mathsfit{s},\mathsfit{a}\right)}}
\\
&=
\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a} \in \mathcal{A}\left(\mathsfit{s}\right)} {\left({\sum\limits_{t=0}^{+\infty}{\gamma^t{\Pr}_\pi\left[\mathsfit{S}_t=\mathsfit{s},{\mathsfit{A}_t}=\mathsfit{a}\right]}}\right)r\left(\mathsfit{s},\mathsfit{a}\right)}
\\
&=
\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right)} {\left(\sum\limits_{t=0}^{+\infty}{\gamma^t{\Pr}_\pi\left[\mathsfit{S}_t=\mathsfit{s},\mathsfit{A}_t=\mathsfit{a}\right]}\right)r\left(\mathsfit{s},\mathsfit{a}\right)}
\\
&=
\sum\limits_{\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right)} {\rho_\pi\left(\mathsfit{s},\mathsfit{a}\right)r\left(\mathsfit{s},\mathsfit{a}\right)}
&
\text{due to definition of }\rho_\pi\left(\mathsfit{s},\mathsfit{a}\right)
\\
&=
{\mathrm{E}_{\left(\mathsfit{S},\mathsfit{A}\right)\sim\rho_\pi}}\left[r\left(\mathsfit{S},\mathsfit{A}\right)\right]
.
\end{array}
$$

The proof completes.)

***Note:*** We have seen the way to convert between expectation over policy trajectory and the expectation over discounted distribution. This method will be repeatedly used in later chapters in the book.
