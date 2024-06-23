# 《强化学习：原理与Python实战》更新与勘误

（2023年07月第1版第1次印刷）

行数计算方法：行数从1开始数起，正文和通栏数学表达式均算，图表、算法不算。


## 第15页代码清单1-2中下面这行

```0.3 * (position + 0.9) ** 4 - 0.008)```

#### 增加缩进


## 第23页第1组通栏数学表达式

$\Pr\left[\mathsfit{S}_ {t_ {i+1}}=\mathsfit{s}_ {t_ {i+1}}\middle\vert \mathsfit{S}_ {t_ 0}=\mathsfit{s}_ 0,\mathsfit{S}_ {t_ 1}=\mathsfit{s}_ 1,\ldots,\mathsfit{S}_ {t_ i}=\mathsfit{s}_ i\right]=\Pr\left[\mathsfit{S}_ {t_ {i+1}}=\mathsfit{s}_ {i+1}\middle\vert \mathsfit{S}_ {t_ i}=\mathsfit{s}_ i\right]$

#### 改为

$\Pr\left[\mathsfit{S}_ {t_ {i+1}}=\mathsfit{s}_ {i+1}\middle\vert \mathsfit{S}_ {t_ 0}=\mathsfit{s}_ 0,\mathsfit{S}_ {t_ 1}=\mathsfit{s}_ 1,\ldots,\mathsfit{S}_ {t_ i}=\mathsfit{s}_ i\right]=\Pr\left[\mathsfit{S}_ {t_ {i+1}}=\mathsfit{s}_ {i+1}\middle\vert \mathsfit{S}_ {t_ i}=\mathsfit{s}_ i\right]$


## 第27页倒数第2组通栏数学表达式的下面一行

$\gamma+\gamma\sum\limits_ {\tau=1}^{+\infty}{\gamma^\tau R_ {\left(t+1\right)+\tau+1}}$

#### 改为

$\gamma+\gamma\sum\limits_ {\tau=0}^{+\infty}{\gamma^\tau R_ {\left(t+1\right)+\tau+1}}$


## 第30页第2组通栏数学表达式

$\mathrm{E}_ \pi$

#### 改为

$\mathrm{E}$


## 第37页最后1行和第38页前3行（共4处）

$\sum\limits_ {t=1}^{+\infty}$

#### 改为

$\sum\limits_ {t=0}^{+\infty}$


## 第38页倒数第2个通栏数学表达式最后的部分

（ $\mathsfit{s}'\in\mathcal{S}$ ）

#### 改为

$\mathsfit{s}\in\mathcal{S}$


## 第40页第5组通栏数学表达式

$\rho\left(\mathsfit{s}'\right)=\sum\limits_ {\mathsfit{s}_ 0\in\mathcal{S}}{p_ {\mathsfit{S}_ 0}\left(\mathsfit{s}\right)\sum\limits_ {t=0}^{+\infty}{\sum\limits_ {\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right)}\gamma^t\Pr_ \pi\left[\mathsfit{S}_ t=\mathsfit{s}'\middle\vert\mathsfit{S}_ 0=\mathsfit{s}\right]}}=\rho_ \pi\left(\mathsfit{s}'\right)$

#### 改为

$\rho\left(\mathsfit{s}'\right)=\sum\limits_ {t=0}^{+\infty}{\gamma^t\sum\limits_ {\mathsfit{s}_ 0\in\mathcal{S}}\Pr_\pi\left[\mathsfit{S}_ t=\mathsfit{s}'\middle\vert\mathsfit{S}_ 0=\mathsfit{s}_ 0\right]p_ {\mathsfit{S}_ 0}\left(\mathsfit{s}_ 0\right)}=\sum\limits_ {t=0}^{+\infty}{\gamma^t\Pr_ \pi\left[\mathsfit{S}_ t=\mathsfit{s}'\right]}=\rho_ \pi\left(\mathsfit{s}'\right)$

注：在这里的证明中，在证明了 $\rho\left(\mathsfit{s}\right)$ 满足 Bellman 期望方程后，说明了它是不动点。由于 $\rho_ \pi\left(\mathsfit{s}\right)$ 也满足同样的 Bellman 期望方程，由不动点的唯一性可得 $\rho\left(\mathsfit{s}\right)=\rho_ \pi\left(\mathsfit{s}\right)$ 。


## 第41页第1组通栏数学表达式第4行

这里用到了全概率公式

#### 改为

这里用到了全期望公式


## 第41页第1组通栏数学表达式倒数第3行

#### 它和倒数第4行重复了，删去重复的行。


## 第42页第2组通栏数学表达式

$p_ \ast\left(\mathsfit{s'},\mathsfit{a'}\middle\vert\mathsfit{s},\mathsfit{a}\right)=\sum\limits_ {\mathsfit{a'}}{\pi_ \ast\left(\mathsfit{a'}\middle\vert\mathsfit{s'} \right)\sum\limits_ \mathsfit{a}{p\left(\mathsfit{s'}\middle\vert\mathsfit{s},\mathsfit{a}\right)}}$,

$\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right),\mathsfit{s'}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s'}\right)$

#### 改为

$p_ \ast\left({\mathsfit{s'},\mathsfit{a'}|\mathsfit{s},\mathsfit{a}}\right)=\pi_ \ast\left(\mathsfit{a'}\middle\vert\mathsfit{s'}\right)p\left( \mathsfit{s'}\mid\mathsfit{s},\mathsfit{a}\right),\quad\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}\left(\mathsfit{s}\right),\mathsfit{s'}\in\mathcal{S},\mathsfit{a'}\in\mathcal{A}\left(\mathsfit{s'}\right)$


## 第49页知识卡片里第2组通栏数学表达式第1行

$\mathop{\text{minimize}}\limits_\mathbfit{y}$

#### 改为

$\mathop{\text{maximize}}\limits_\mathbfit{y}$


## 第49页知识卡片里最后一行

$\mathbfit{y}\geqslant0$

#### 改为

$\mathbfit{y}\geqslant\mathbf{0}$


## 第62页第2组通栏数学表达式

$\pi\left(\mathsfit{a}\middle\vert\mathsfit{s}'\right)\left(q'\left(\mathsfit{s},\mathsfit{a}\right)-q''\left(\mathsfit{s},\mathsfit{a}\right)\right)$

#### 改为

$\pi\left(\mathsfit{a}'\middle\vert\mathsfit{s}'\right)\left(q'\left(\mathsfit{s}',\mathsfit{a}'\right)-q''\left(\mathsfit{s}',\mathsfit{a}'\right)\right)$


## 第61页最后1组通栏数学表达式第1行

$\max\limits_ {\mathsfit{s}'}\left|v'\left(\mathsfit{s}'\right)-v''\left(\mathsfit{s}'\right)\right|$

#### 改为

$\max\limits_ {\mathsfit{s}''}\left|v'\left(\mathsfit{s}''\right)-v''\left(\mathsfit{s}''\right)\right|$


## 第62页第3组通栏数学表达式

$\leqslant\gamma\sum\limits_ {\mathsfit{s}'}p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}\right)\sum\limits_ {\mathsfit{a}'}\pi\left(\mathsfit{a}\middle\vert\mathsfit{s}'\right)\max\limits_ {\mathsfit{s}',\mathsfit{a}'}\left|q'\left(\mathsfit{s},\mathsfit{a}\right)-q''\left(\mathsfit{s},\mathsfit{a}\right)\right|$

$=\gamma\sum\limits_ {\mathsfit{s}'}p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}\right)\sum\limits_ {\mathsfit{a}'}\pi\left(\mathsfit{a}\middle\vert\mathsfit{s}'\right)d_ \infty\left(q',q''\right)$

#### 改为

$\leqslant\gamma\sum\limits_ {\mathsfit{s}'}p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}\right)\sum\limits_ {\mathsfit{a}'}\pi\left(\mathsfit{a}'\middle\vert\mathsfit{s}'\right)\max\limits_ {\mathsfit{s}'',\mathsfit{a}''}\left|q'\left(\mathsfit{s}'',\mathsfit{a}''\right)-q''\left(\mathsfit{s}'',\mathsfit{a}''\right)\right|$

$=\gamma\sum\limits_ {\mathsfit{s}'}p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}\right)\sum\limits_ {\mathsfit{a}'}\pi\left(\mathsfit{a}'\middle\vert\mathsfit{s}'\right)d_ \infty\left(q',q''\right)$


## 第62页最后一组数学表达式第3行和第4行（共2处）

$p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}'\right)$

#### 改为

$p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}\right)$


## 第63页第2组通栏数学表达式第4行

$=\gamma\sum\limits_{\mathsfit{s}'\in\mathcal{S}}{p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}\right)d_\infty\left(q',q''\right)}$

#### 改为

$\leqslant\gamma\sum\limits_{\mathsfit{s}'\in\mathcal{S}}{p\left(\mathsfit{s}'\middle\vert\mathsfit{s},\mathsfit{a}\right)d_\infty\left(q',q''\right)}$


## 第66页算法3.3第1.2步

$\pi\left(\mathsfit{s}\right)=\arg\max_ \mathsfit{\mathsfit{a}}{q\left(\mathsfit{s},\mathsfit{a}\right)}$

#### 改为

$\pi\left(\mathsfit{s}\right)\leftarrow\arg\max_ \mathsfit{\mathsfit{a}}{q\left(\mathsfit{s},\mathsfit{a}\right)}$


## 第67页算法3.4第2.2步

$\mathsfit{a}'=\arg\max_ \mathsfit{\mathsfit{a}}{q\left(\mathsfit{s},\mathsfit{a}\right)}$

#### 改为

$\mathsfit{a}'\leftarrow\arg\max_ \mathsfit{\mathsfit{a}}{q\left(\mathsfit{s},\mathsfit{a}\right)}$


## 第69页算法3-8第1步（共2处）

$v_ 0$

#### 改为

$v$


## 第73页正文第2行

$\pi\left(\mathsfit{s},\mathsfit{a}\right)=\frac{1}{\left|\mathcal{A}\right|}$

#### 改为

$\pi\left(\mathsfit{a}\middle\vert\mathsfit{s}\right)=\frac{1}{\left|\mathcal{A}\right|}$


## 第80页倒数第5组通栏数学表达式第2行

$\alpha_ k\mathrm{E}\left[\left|F{\left(X_ {k-1}\right)}^2\right|\middle\vert{X}_ {k-1}\right]$

#### 改为

$\alpha_ k\mathrm{E}\left[\left|F\left(X_ {k-1}\right)\right|^2\middle\vert{X}_ {k-1}\right]$


## 第89页算法4.8第2.1步

策略 $\pi$ 来生成

#### 改为

策略来生成


## 第91页第1组通栏数学表达式第2行

$p\left(\mathsfit{S}_ T,R_ T\middle\vert\mathsfit{S}_ {T-1},A_ {T-1}\right)$

#### 改为

$p\left(\mathsfit{S}_ T,R_ T\middle\vert\mathsfit{S}_ {T-1},\mathsfit{A}_ {T-1}\right)$


## 第113页算法5.4第2.2.3步

$q\left(\mathsfit{S},\mathsfit{A}\right)\leftarrow q\left(\mathsfit{S},\mathsfit{A}\right)+\alpha\left[U-q\left(\mathsfit{S},\mathsfit{A}\right)\right]$

#### 改为

$q\left(\mathsfit{S}_ t,\mathsfit{A}_ t\right)\leftarrow q\left(\mathsfit{S}_ t,\mathsfit{A}_ t\right)+\alpha\left[U-q\left(\mathsfit{S}_ t,\mathsfit{A}_ t\right)\right]$


## 第113页算法5.5第2.2.2步

更新 $v\left(\mathsfit{S}\right)$ 以减小 $\left[U-v\left(\mathsfit{S}\right)\right]^2$ .

#### 改为

更新 $v\left(\mathsfit{S}_ t\right)$ 以减小 $\left[U-v\left(\mathsfit{S}_ t\right)\right]^2$ .


## 第115页正文第一段

它也仅仅是在多步时序差分动作价值估计算法的基础上加入了策略改进的步骤。

#### 改为

它与多步时序差分动作价值估计算法相比，在采样时使用了由最新的动作价值决定的策略。


## 第117页算法5-10第2.2.3步

需要根据 $q\left(\mathsfit{S}\right)$ 修改 $\pi\left(\cdot\middle\vert\mathsfit{S}\right)$ .

#### 改为

需要根据 $q\left(\mathsfit{S}_ t\right)$ 修改 $\pi\left(\cdot\middle\vert\mathsfit{S}_ t\right)$ .


## 第117页算法5-10第2.2.4步第2行

$q\left(\mathsfit{S}_ {t+n}\middle\vert\cdot\right)$

#### 改为

$q\left(\mathsfit{S}_ {t+n},\cdot\right)$


## 第117页最后一组通栏数学表达式

$\rho_ {t+1:t+n-1}=\frac{\Pr_ \pi\left[R_ {t+1},\mathsfit{S}_ {t+1},\mathsfit{A}_ {t+1},\ldots,\mathsfit{S}_ {t+n}\middle\vert\mathsfit{S}_ t\right]}{\Pr_ b\left[R_ {t+1},\mathsfit{S}_ {t+1},\mathsfit{A}_ {t+1},\ldots,\mathsfit{S}_ {t+n}\middle\vert\mathsfit{S}_ t\right]}=\prod\limits_ {\tau=t+1}^{t+n-1}{\frac{\pi\left(\mathsfit{A}_ \tau\middle\vert\mathsfit{S}_ \tau\right)}{b\left(\mathsfit{A}_ \tau\middle\vert\mathsfit{S}_ \tau\right)}}$

#### 改为

$\rho_ {t+1:t+n-1}=\frac{\Pr_ \pi\left[R_ {t+1},\mathsfit{S}_ {t+1},\mathsfit{A}_ {t+1},\ldots,\mathsfit{S}_ {t+n}\mid\mathsfit{S}_ t,\mathsfit{A}_ t\right]}{\Pr_ b\left[R_ {t+1},\mathsfit{S}_ {t+1},\mathsfit{A}_ {t+1},\ldots,\mathsfit{S}_ {t+n}\mid\mathsfit{S}_ t,\mathsfit{A}_ t\right]}=\prod\limits_ {\tau=t+1}^{t+n-1}{\frac{\pi\left(\mathsfit{A}_ \tau\middle\vert\mathsfit{S}_ \tau\right)}{b\left(\mathsfit{A}_ \tau\middle\vert\mathsfit{S}_ \tau\right)}}$


## 第177页最后一行

$\gamma^2\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}\left[\nabla{v_ {\pi\left(\boldsymbol\theta\right)}}\left(\mathsfit{S}_ 1\right)\right]$

#### 改为

$\gamma^2\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}\left[\nabla{v_ {\pi\left(\boldsymbol\theta\right)}}\left(\mathsfit{S}_ 2\right)\right]$


## 第180页第1组通栏数学表达式

$\boldsymbol\theta_ {t+1}\leftarrow\boldsymbol\theta_ t+\alpha\gamma^t G_t\nabla\ln\pi\left(\mathsfit{A}_ t\middle\vert\mathsfit{S}_ t;\boldsymbol\theta\right),\quad t=0,1,\cdots$

#### 改为

$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\gamma^t G_t\nabla\ln\pi\left(\mathsfit{A}_ t\middle\vert\mathsfit{S}_ t;\boldsymbol\theta\right)$


## 第183行算法7-3第2.4.2步第1行

$\gamma^t G_ t$

#### 改为

$\gamma^t G$


## 第206页知识卡片“Fisher信息矩阵”内文第2段第1行

$\sum\limits_\mathsfit{x}{p\left(\mathsfit{x};\boldsymbol\theta\right)\nabla\ln p\left(\mathsfit{X};\boldsymbol\theta\right)}=\sum\limits_\mathsfit{x}{\nabla p\left(\mathsfit{X};\boldsymbol\theta\right)}=\nabla\sum\limits_\mathsfit{x}{p\left(\mathsfit{X};\boldsymbol\theta\right)}$

#### 改为

$\sum\limits_\mathsfit{x}{p\left(\mathsfit{x};\boldsymbol\theta\right)\nabla\ln p\left(\mathsfit{x};\boldsymbol\theta\right)}=\sum\limits_\mathsfit{x}{\nabla p\left(\mathsfit{x};\boldsymbol\theta\right)}=\nabla\sum\limits_\mathsfit{x}{p\left(\mathsfit{x};\boldsymbol\theta\right)}$


## 第208页第8.4.2节正文第1段倒数第2行

比 $g_{\pi\left(\boldsymbol\theta_ k\right)}$ 小

#### 改为

比 $g_{\pi\left(\boldsymbol\theta\right)}$ 小


## 第209页倒数第3组通栏数学表达式

$\boldsymbol{0}+\mathbfit{g}\left({\boldsymbol\theta}_ k\right)\left({\boldsymbol\theta}-{\boldsymbol\theta}_ k\right)$

#### 改为

$0+\left[\mathbfit{g}\left({\boldsymbol\theta}_ k\right)\right]^\mathrm{T}\left({\boldsymbol\theta}-{\boldsymbol\theta}_ k\right)$


## 第209页倒数第2组通栏数学表达式第1行

$\mathbfit{g}\left({\boldsymbol\theta}_ k\right)\left({\boldsymbol\theta}-{\boldsymbol\theta}_ k\right)$

#### 改为

$\left[\mathbfit{g}\left({\boldsymbol\theta}_ k\right)\right]^\mathrm{T}\left({\boldsymbol\theta}-{\boldsymbol\theta}_ k\right)$


## 第252页正文倒数第2~3行

在2.4.3步和2.4.5步

#### 改为

在第2.4.5步


## 第256页第2个通栏数学表达式


$\int_0^t{e^{\theta\left(\tau-t\right)}dB_ t}$

#### 改为

$\int_0^t{e^{\theta\left(\tau-t\right)}dB_ \tau}$


## 第271页最后一组通栏数学表达式最后一行

$v_ \pi^\left(\text{H}\right)\left(\mathsfit{s},\mathsfit{a}\right)$

#### 改为

$v_ \pi^\left(\text{H}\right)\left(\mathsfit{s}\right)$


## 第273页10.1.3节小节标题之前的一组通栏数学表达式

$\pi_ \pi^{\left(\text{H}\right)}$

#### 改为

$\pi$


## 第272页第2组通栏数学表达式

$\sum\limits_ {\mathsfit{a}}$

#### 改为

$\sum\limits_ {\mathsfit{a}'}$


## 第272页第3组通栏数学表达式

$\mathrm{E}_ {\left(\mathsfit{s},\mathsfit{a}\right)\sim\rho_ \pi}\left[q_ \pi^{\left(\mathrm{H}\right)}\left(\mathsfit{s},\mathsfit{a}\right)\right]$

#### 改为

$\mathrm{E}_ {\left(\mathsfit{S},\mathsfit{A}\right)\sim\rho_ \pi}\left[q_ \pi^{\left(\mathrm{H}\right)}\left(\mathsfit{S},\mathsfit{A}\right)\right]$


## 第273页第1组通栏数学表达式

$\mathrm{E}_ {\left(\mathsfit{s},\mathsfit{a}\right)\sim\rho_ \pi}\left[q_ \pi^{\left(\text{soft}\right)}\left(\mathsfit{s},\mathsfit{a}\right)+\alpha^{\left(\mathrm{H}\right)}\mathrm{H}\left[\pi\left(\cdot\middle\vert\mathsfit{s}\right)\right]\right]$

#### 改为

$\mathrm{E}_ {\left(\mathsfit{S},\mathsfit{A}\right)\sim\rho_ \pi}\left[q_ \pi^{\left(\text{soft}\right)}\left(\mathsfit{S},\mathsfit{A}\right)+\alpha^{\left(\mathrm{H}\right)}\mathrm{H}\left[\pi\left(\cdot\middle\vert\mathsfit{S}\right)\right]\right]$


## 第276页最后一组通栏数学表达式（两处）

$\mathrm{E}_ {\pi\left(\theta\right)}$

#### 改为

$\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}$


## 第277页第2组通栏数学表达式最后一行

$\mathrm{E}_ \pi$

#### 改为

$\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}$


## 第279页第1行

$\gamma\sum\limits_ \mathsfit{s'}{p_ {\pi\left(\boldsymbol\theta\right)}\left(\mathsfit{s'}\middle\vert\mathsfit{s}\right)\nabla v_ {\pi\left(\boldsymbol\theta\right)}^\left(\mathrm{H}\right)\left(\mathsfit{s}\right)}$

### 改为

$\gamma\sum\limits_ \mathsfit{s'}{p_ {\pi\left(\boldsymbol\theta\right)}\left(\mathsfit{s'}\middle\vert\mathsfit{s}\right)\nabla v_ {\pi\left(\boldsymbol\theta\right)}^\left(\mathrm{H}\right)\left(\mathsfit{s'}\right)}$


## 第279页第3~4行

$\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}\left[\sum\limits_ \mathsfit{a}q_ {\pi\left(\boldsymbol\theta\right)}^\left(\mathrm{H}\right)\left(\mathsfit{S}_ t,\mathsfit{a}\right)\nabla\pi\left(\mathsfit{a}\middle\vert{\mathsfit{S}_ t};\boldsymbol\theta\right)\right]+$

$\nabla\left(\alpha^\left(\mathrm{H}\right)\mathrm{H}\left[\pi\left(\cdot\middle\vert\mathsfit{S}_ t;\boldsymbol\theta\right)\right]\right)$

### 改为

$\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}\left[\sum\limits_ \mathsfit{a}q_ {\pi\left(\boldsymbol\theta\right)}^\left(\mathrm{H}\right)\left(\mathsfit{S}_ t,\mathsfit{a}\right)\nabla\pi\left(\mathsfit{a}\middle\vert{\mathsfit{S}_ t};\boldsymbol\theta\right)+\nabla\left(\alpha^\left(\mathrm{H}\right)\mathrm{H}\left[\pi\left(\cdot\middle\vert\mathsfit{S}_ t;\boldsymbol\theta\right)\right]\right)\right]$


## 第279页第6行

$\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}\left[\sum\limits_ \mathsfit{a}q_ {\pi\left(\boldsymbol\theta\right)}^\left(\mathrm{H}\right)\left(\mathsfit{S}_ t,\mathsfit{a}\right)\nabla\pi\left(\mathsfit{a}\middle\vert{\mathsfit{S}_ t};\boldsymbol\theta\right)\right]+\nabla\left(\alpha^\left(\mathrm{H}\right)\mathrm{H}\left[\pi\left(\cdot\middle\vert\mathsfit{S}_ t\right)\right]\right)$

### 改为

$\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}\left[\sum\limits_ \mathsfit{a}q_ {\pi\left(\boldsymbol\theta\right)}^\left(\mathrm{H}\right)\left(\mathsfit{S}_ t,\mathsfit{a}\right)\nabla\pi\left(\mathsfit{a}\middle\vert{\mathsfit{S}_ t};\boldsymbol\theta\right)+\nabla\left(\alpha^\left(\mathrm{H}\right)\mathrm{H}\left[\pi\left(\cdot\middle\vert\mathsfit{S}_ t;\boldsymbol\theta\right)\right]\right)\right]$


## 第280页第1组通栏数学表达式最后1行

$\mathrm{E}_ {\pi\left(\boldsymbol\theta\right)}\left[\left(q_ {\pi\left(\boldsymbol\theta\right)}^{\left(柔\right)}\left(\mathsfit{s},\mathsfit{a}\right)-\alpha^{\left(\text{H}\right)}\left(\ln\pi\left(\mathsfit{a}\middle\vert\mathsfit{s};\boldsymbol\theta\right)+1\right)\right)\nabla\ln\pi\left(\mathsfit{a}\middle\vert\mathsfit{s};\boldsymbol\theta\right)\right]$

#### 改为

$\mathrm{E}_ {\mathsfit{A}\sim\pi\left(\cdot\middle\vert\mathsfit{s};\boldsymbol\theta\right)}\left[\left(q_ {\pi\left(\boldsymbol\theta\right)}^{\left(柔\right)}\left(\mathsfit{s},\mathsfit{A}\right)-\alpha^{\left(\text{H}\right)}\left(\ln\pi\left(\mathsfit{A}\middle\vert\mathsfit{s};\boldsymbol\theta\right)+1\right)\right)\nabla\ln\pi\left(\mathsfit{A}\middle\vert\mathsfit{s};\boldsymbol\theta\right)\right]$


## 第283页第3组通栏数学表达式两行各有一处共两处

$\mathrm{E}_{\mathsfit{A}'\sim\pi\left(\boldsymbol\theta\right)}$

#### 改为

$\mathrm{E}_{\mathsfit{A}'\sim\pi\left(\cdot\middle\vert\mathsfit{s};\boldsymbol\theta\right)}$


## 第284页算法10-2第2.2.2.2步，第285页算法10-3第2.2.2.3步（共2处）

$U_ t^{\left(q\right)}\leftarrow R_ {t+1}+$

#### 改为

$U^{\left(q\right)}\leftarrow R+$


## 第284页算法10-2第2.2.2.3步，第285页算法10-3第2.2.2.4步（共2处）

$U_ t^{\left(q\right)}$

#### 改为

$U^{\left(q\right)}$


## 第284页算法10-2第2.2.2.2步和第2.2.2.3步，第285页算法10-3第2.2.2.3步，第286页算法10-3第2.2.2.4步（共4处）

$U_ t^{\left(v\right)}$

#### 改为

$U^{\left(v\right)}$


## 第285页算法10-3第2.2.2.2步

#### 删去

（ $(\mathsfit{S},\mathsfit{A},R$

$\mathsfit{S}',D')\in\mathcal{B}$ ）


## 第288页代码清单10-2

```python
    def step(self, observation, reward, terminated):
        position, velocity = observation
        if position > -4 * velocity or position < 13 * velocity - 0.6:
            force = 1.
        else:
            force = -1.
        action = np.array([force,])
        return action
```

#### 改为

```python
    def step(self, observation, reward, terminated):
        x, y, v_ x, v_ y, angle, v_ angle, contact_ left, \
                contact_ right = observation

        if contact_ left or contact_ right:  # 腿接触了
            f_ y = -10. * v_ y - 1.
            f_ angle = 0.
        else:
            f_ y = 5.5 * np.abs(x) - 10. * y - 10. * v_ y - 1.
            f_ angle = -np.clip(5. * x + 10. * v_ x, -4, 4
                    ) + 10. * angle + 20. * v_ angle

        action = np.array([f_ y, f_ angle])
        return action
```


## 第322页正文第2段第1行

在 $\left(Q_ p,d_{\mathrm{supW},p}\right)$ 上

#### 改为

在 $\left(\mathcal{Q}_ p,d_{\mathrm{supW},p}\right)$ 上


## 第326页倒数第2行

类别分布 $p^{\left(\cdot\right)}\left(\cdot,\cdot\right)$ 和自

#### 改为

类别分布 $p^{\left(\cdot\right)}\left(\cdot,\cdot;\boldsymbol{w}\right)$ 和自


## 第328页算法12-1第2.2.2.4步最后一行，第329页算法12-2第2.2.2.4步第三行（各一处，共2处）

$\sum\limits_{i\in\mathcal{I}}$

#### 改为

$\sum\limits_{j\in\mathcal{I}}$


## 第330-331页知识卡片第2-5段

考虑随机变量 $X$ 的在给定累积概率值 $\omega\in\left[0,1\right]$ 下的分位数 $\phi_ X\left(\omega\right)$。 $\phi_ X\left(\omega\right)>X$ 的概率是 $\omega$，……

（证明：……

所以，……

如果……0，按照权重 $1-\omega$ 来试图增加 $\delta$。）

#### 改为

考虑随机变量 $X$ 的在给定累积概率值 $\omega\in\left[0,1\right]$ 下的分位数 $\phi_ X\left(\omega\right)$。 $X<\phi_ X\left(\omega\right)$ 的概率是 $\omega$，即 $X-\phi_ X\left(\omega\right)<0$ 的概率是 $\omega$。记 $\phi_ X\left(\omega\right)$ 的估计值为 $\hat\phi$，可以通过观测 $X-\hat\phi<0$ 的概率来评估这个估计是否准确：如果 $X-\hat\phi<0$ 的概率小于 $\omega$，即 $X<\hat\phi$ 的概率小于 $\omega$，那么说明估计值 $\hat\phi$ 太小了，应该增加这个估计值；如果 $X-\hat\phi<0$ 的概率大于  $\omega$，即 $X<\hat\phi$ 的概率大于 $\omega$，那么说明估计值 $\hat\phi$ 太大了，应该减小这个估计值。具体在优化过程中，可以通过最小化 $\mathrm{E}\left[\left(\omega-1_ {X-\phi<0}\right)\left(X-\phi\right)\right]$ 来估计分位函数。（证明：为了简单，只考虑 $X$ 是连续随机变量的情况。注意到

 $\mathrm{E}\left[\left(\omega-1_ {X-\phi<0}\right)\left(X-\phi\right)\right]$ 

 $=-\omega\phi+\omega\mathrm{E}\left[X\right]+\phi\mathrm{E}\left[1_ {X-\phi<0}\right]-\mathrm{E}\left[1_ {X-\phi<0}X\right]$ 

 $=-\omega\phi+\omega\mathrm{E}\left[X\right]+\phi\int_ {x\in\mathcal{X}:x<\phi}{p\left(x\right)\mathrm{d}x}-\phi\int_ {x\in\mathcal{X}:x<\phi}{xp\left(x\right)\mathrm{d}x}$ , 

进而有

$\frac{\mathrm{d}}{\mathrm{d}\phi}\mathrm{E}\left[\left(\omega-1_ {X-\phi<0}\right)\left(X-\phi\right)\right]$ 

 $=\frac{\mathrm{d}}{\mathrm{d}/phi}\left[-\omega\phi+\omega\mathrm{E}\left[X\right]+\phi\int_ {x\in\mathcal{X}:x<\phi}{p\left(x\right)\mathrm{d}x}-\phi\int_ {x\in\mathcal{X}:x<\phi}{xp\left(x\right)\mathrm{d}x}\right]$

$=-\omega+0+\left[\int_ {x\in\mathcal{X}:x<\phi}{p\left(x\right)\mathrm{d}x}+\phi p\left(\phi\right)\right]-\phi p\left(\phi\right)$

$=-\omega+\int_ {x\in\mathcal{X}:x<\phi}{p\left(x\right)\mathrm{d}x}$

令 $\frac{\mathrm{d}}{\mathrm{d}\phi}\mathrm{E}\left[\left(\omega-1_ {X-\phi<0}\right)\left(X-\phi\right)\right]=0$  可解得 $\int_ {x\in\mathcal{X}:x<\phi}{p\left(x\right)\mathrm{d}x}=\omega$。所以在优化目标极值点处， $\phi$ 是随机变量累积概率值 $\omega$ 处对应的分位数。）所以，在训练过程中获得了样本值 $x_ 0,x_ 1,x_ 2,\ldots,x_ {c--1}$ ，可以试图最小化给定分位数 $\omega$ 下的**分位数回归损失**（Quantile Regression loss，QR loss）：

$\frac1c\sum\limits_ {i=0}^{c-1}{\ell_ \text{QR}\left(x_ i-\phi\right)}$

其中 $\ell_ \text{QR}=\left(\omega-1_ {\delta<0}\right)\delta$ 是每个样本的样本损失。这里的 $\ell_ \text{QR}=\left(\omega-1_ {\delta<0}\right)\delta$ 也可以写成 $\ell_ \text{QR}=\left|\omega-1_ {\delta<0}\right|\left|\delta\right|$ 。如果预测值过小，则 $\delta>0$ ，那么按照权重 $\omega$ 来试图增加  $\delta$ 。如果预测值过大，则 $\delta<0$，按照权重 $\left(1-\omega\right)$ 来试图减小 $\delta$ 。


## 第336页（12.5节正文，共2处）、第356页（12.7节本章要点正文内，共2处）、第357页（单选题(5)的三个选项，共3处）

累计概率

#### 改为

累积概率


## 第363页倒数第13行

所以对于 $\varepsilon=\sqrt{\frac{2\ln\kappa}{c_ \ast}}>0$ ，有

#### 改为

所以对于 $\varepsilon=\sqrt{\frac{2\ln\kappa}{c_ \mathsfit{a}}}>0$ ，有


## 第363页倒数第10行

#### 增加文字

记 $\mathsfit{a}_ \ast$ 是最优动作。

作者注：把 $c=c_\mathsfit{a}$ ， $\bar{X}=\tilde{q}_ {c_ \mathsfit{a}}\left(\mathsfit{a}\right)$ ，和 $\varepsilon=\sqrt{\frac{2\ln\kappa}{c_ \mathsfit{a}}}$ 代入Hoeffding不等式 $\Pr\left[\bar{X}-\mathrm{E}\left[\bar{X}\right]\geqslant\varepsilon\right]\leqslant\exp\left(-2c\varepsilon^2\right)$ 和 $\Pr\left[\bar{X}-\mathrm{E}\left[\bar{X}\right]\leqslant-\varepsilon\right]\leqslant\exp\left(-2c\varepsilon^2\right)$ ，有 $\Pr\left[\tilde{q}_ {c_ \mathsfit{a}}\left(\mathsfit{a}\right)-q\left(\mathsfit{a}\right)\geqslant\sqrt{\frac{2\ln\kappa}{c_ \mathsfit{a}}}\right]\leqslant\frac{1}{\kappa^4}$ 和 $\Pr\left[\tilde{q}_ {c_ \mathsfit{a}}\left(\mathsfit{a}\right)-q\left(\mathsfit{a}\right)\leqslant-\sqrt{\frac{2\ln\kappa}{c_ \mathsfit{a}}}\right]\leqslant\frac{1}{\kappa^4}$ ，所以 $\Pr\left[q\left(\mathsfit{a}\right)+\sqrt{\frac{2\ln\kappa}{c_\mathsfit{a}}}\leqslant\tilde{q}_ {c_ \mathsfit{a}}\left(\mathsfit{a}\right)\right]\leqslant\frac{1}{\kappa^4}$ 和 $\Pr\left[\tilde{q}_ {c_ \mathsfit{a}}\left(\mathsfit{a}\right)+\sqrt{\frac{2\ln\kappa}{c_ \mathsfit{a}}}\leqslant q\left(\mathsfit{a}\right)\right]\leqslant\frac{1}{\kappa^4}$ 。在后面那个式子中取 $\mathsfit{a}=\mathsfit{a}_ \ast$ 和 $c_ \ast=c_ \mathsfit{a}$ 得证。


## 第363页倒数第4行

于任意的正整数 $c_ \mathsfit{a}\geqslant\underline{c}_ \kappa\left(\mathsfit{a}\right)$ ，有 $q\left(\mathsfit{a}_ \ast\right)\le q\left(\mathsfit{a}\right)+\sqrt{\frac{2\ln\kappa}{c_ \mathsfit{a}}}+\sqrt{\frac{2\ln\kappa }{c_ \mathsfit{a}}}$

#### 改为

于任意的正整数 $c_ \mathsfit{a}>\underline{c}_ \kappa\left(\mathsfit{a}\right)$ ，有 $q\left(\mathsfit{a}_ \ast\right)>q\left(\mathsfit{a}\right)+\sqrt{\frac{2\ln\kappa}{c_ \mathsfit{a}}}+\sqrt{\frac{2\ln\kappa }{c_ \mathsfit{a}}}$


## 第363页倒数第2行

$c_ \mathsfit{a}\geqslant\underline{c}_ \kappa\left(\mathsfit{a}\right)$

#### 改为

$c_ \mathsfit{a}>\underline{c}_ \kappa\left(\mathsfit{a}\right)$


## 第365页倒数第6行，第365页第2行（共2处）

$c_ \kappa\left(\mathsfit{a}\right)\geqslant\underline{c}_ \kappa\left(\mathsfit{a}\right)$

#### 改为

$c_ \kappa\left(\mathsfit{a}\right)>\underline{c}_ \kappa\left(\mathsfit{a}\right)$


## 第367页算法13-3第1.1步最后一行

$\text{normal}\left(\mu\left(\mathsfit{a}\right),\sigma\left(\mathsfit{a}\right)\right)$

#### 改为

$\text{normal}\left(\mu\left(\mathsfit{a}\right),\sigma^2\left(\mathsfit{a}\right)\right)$


## 第368页算法13-4第2.3步

动作 $A$

#### 改为

动作 $\mathsfit{A}$


## 第371页第17行

$1-{\left({\mathrm{E}\left[\mathbfit{\hat{p}}_ i\left(X_ i\right)\right]}\right)^\mathrm{T}}\mathbfit{p}+\left\|\mathbfit{p}\right\|_ 2^2$

#### 改为

$1-2{\left({\mathrm{E}\left[\mathbfit{\hat{p}}_ i\left(X_ i\right)\right]}\right)^\mathrm{T}}\mathbfit{p}+\left\|\mathbfit{p}\right\|_ 2^2$


## 第372页倒数第8行

$2\exp\left(-\frac{2c_ {\kappa,t}\left(\mathsfit{s},\mathsfit{a}\right)\varepsilon^2}{t_ \max^2}\right)=\frac{1}{\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}$

#### 改为

$2\exp\left(-\frac{2c_ {\kappa,t}\left(\mathsfit{s},\mathsfit{a}\right)\varepsilon^2}{g_ \max^2}\right)=\frac{1}{\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}$


## 第372页倒数第6行

$\Pr\left[\left|\sum\limits_ {\mathsfit{s'}}{p_ {\kappa,t}\left(\mathsfit{s'}\middle\vert\mathsfit{s},\mathsfit{a}\right)v_ \ast\left(\mathsfit{s'}\right)}-\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{s},\mathsfit{a}\right)v_ \ast\left(\mathsfit{s'}\right)}\right|
\geqslant{g_ \max}\sqrt{\frac{\ln 2\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}{c_ {\kappa,t}\left(\mathsfit{s},\mathsfit{a}\right)}}\right]$

#### 改为

$\Pr\left[\left|\sum\limits_ {\mathsfit{s'}}{p_ {\kappa,t}\left(\mathsfit{s'}\middle\vert\mathsfit{s},\mathsfit{a}\right)v_ \ast\left(\mathsfit{s'}\right)}-\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{s},\mathsfit{a}\right)v_ \ast\left(\mathsfit{s'}\right)}\right|
\geqslant{g_ \max}\sqrt{\frac{\ln 2\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}{2c_ {\kappa,t}\left(\mathsfit{s},\mathsfit{a}\right)}}\right]$


## 第372页倒数第4行

$\sqrt{\ln2\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}\leqslant2\sqrt{\ln\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}$

#### 改为

$\sqrt{\frac12\ln2\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}\leqslant2\sqrt{\ln\left|\mathcal{S}\right|\left|\mathcal{A}\right|{k^2}t_ \max^2}$


## 第373页倒数第4行，第374页第3行，第374页第5行第10行第11行第12行第15行第16行第19行，第375页第6行第7行第11行。

$u_ {\kappa,t}^{\left(v\right)}\left(\mathsfit{s'}\right)$

#### 改为

$u_ {\kappa,t+1}^{\left(v\right)}\left(\mathsfit{s'}\right)$


## 第374页第7行

$q_ {\pi_ \kappa}\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)=r\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)-\gamma\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)v_ {\pi_ \kappa}\left(\mathsfit{s'}\right)}$

#### 改为

$q_ {\pi_ \kappa}\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)=r\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)+\gamma\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)v_ {\pi_ \kappa}\left(\mathsfit{s'}\right)}$


## 第374页第10-12行

$\quad=b_ {\kappa,t}\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)+\gamma\left(\sum\limits_ {\mathsfit{s'}}{p_ {\kappa,t}\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)u_ {\kappa,t}^\left(v\right)\left(\mathsfit{s'}\right)}-\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)u_ {\kappa,t}^\left(v\right)\left(\mathsfit{s'}\right)}\right)$

$\quad=b_ {\kappa,t}\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)+\gamma\left(\sum\limits_ {\mathsfit{s'}}{\left(p_ {\kappa,t}\left(\mathsfit{s'}\middle\vert{\mathsfit{S}_ {\kappa,t}},\mathsfit{A}_ {\kappa,t}\right)-p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)\right)u_ {\kappa,t}^\left(v\right)\left(\mathsfit{s'}\right)}\right)+$

$\quad\quad\gamma\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)\left(u_ {\kappa,t}^\left(v\right)\left(\mathsfit{s'}\right)-v_ {\pi_ {k\kappa}}\left(\mathsfit{s'}\right)\right)}$

#### 改为

$\quad=b_ {\kappa,t}\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)+\gamma\left(\sum\limits_ {\mathsfit{s'}}{p_ {\kappa,t}\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)u_ {\kappa,t+1}^\left(v\right)\left(\mathsfit{s'}\right)}-\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)v_ {\pi_ \kappa}\left(\mathsfit{s'}\right)}\right)$

$\quad=b_ {\kappa,t}\left(\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)+\gamma\sum\limits_ {\mathsfit{s'}}{\left(p_ {\kappa,t}\left(\mathsfit{s'}\middle\vert{\mathsfit{S}_ {\kappa,t}},\mathsfit{A}_ {\kappa,t}\right)-p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)\right)u_ {\kappa,t+1}^\left(v\right)\left(\mathsfit{s'}\right)}+$

$\quad\quad\gamma\sum\limits_ {\mathsfit{s'}}{p\left(\mathsfit{s'}\middle\vert\mathsfit{S}_ {\kappa,t},\mathsfit{A}_ {\kappa,t}\right)\left(u_ {\kappa,t+1}^\left(v\right)\left(\mathsfit{s'}\right)-v_ {\pi_ \kappa}\left(\mathsfit{s'}\right)\right)}$


## 第382页本章要点第2点

Gaussien

#### 改为

Gaussian


## 第392页正文第4行

$\left(R-r\left(\mathsfit{s},\mathsfit{a}\right)\right)^2$

#### 改为

$\left(R-r\left(\mathsfit{S},\mathsfit{A}\right)\right)^2$


## 第424页最后一行

$\geqslant\mathop\sup\limits_ {\psi:\mathcal{X}\to\mathbb{R}}\sum\limits_ \mathsfit{x}{q\left(\mathsfit{x}\right)\left(\psi\left(\mathsfit{x}\right)\frac{p\left(\mathsfit{x}\right)}{q\left(\mathsfit{x}\right)}-f^\ast\left(\psi\left(\mathsfit{x}\right)\right)\right)}$

#### 改为

$=\mathop\sup\limits_ {\psi:\mathcal{X}\to\mathbb{R}}\sum\limits_ \mathsfit{x}{q\left(\mathsfit{x}\right)\left(\psi\left(\mathsfit{x}\right)\frac{p\left(\mathsfit{x}\right)}{q\left(\mathsfit{x}\right)}-f^\ast\left(\psi\left(\mathsfit{x}\right)\right)\right)}$


## 第425页正文倒数第2个通栏数学表达式最后一行

$d_ \text{TV}\left(\rho_ {\pi'}\left(\cdot,\cdot\right)\middle\|\rho_ {\pi'}\left(\cdot,\cdot\right)\right)$

#### 改为

$d_ \text{TV}\left(\rho_ {\pi'}\left(\cdot,\cdot\right)\middle\|\rho_ {\pi''}\left(\cdot,\cdot\right)\right)$


## 第427页第2组通栏数学表达式

$d_ \rm{TV}\left(\rho_ {\pi'}\left(\cdot,\cdot\right)\middle\|\rho_ {\pi''}\left(\cdot,\cdot\right)\right)\leqslant\frac{\gamma}{1-\gamma}\mathrm{E}_ {\mathsfit{S}\sim\rho_ {\pi''}}\left[d_ \mathrm{TV}\left(\pi'\left(\cdot\middle\vert\mathsfit{S}\right)\middle\|\pi''\left(\cdot\middle\vert\mathsfit{S}\right)\right)\right]$

#### 改为

$d_ \rm{TV}\left(\rho_ {\pi'}\left(\cdot,\cdot\right)\middle\|\rho_ {\pi''}\left(\cdot,\cdot\right)\right)\leqslant\frac{1}{1-\gamma}\mathrm{E}_ {\mathsfit{S}\sim\rho_ {\pi''}}\left[d_ \mathrm{TV}\left(\pi'\left(\cdot\middle\vert\mathsfit{S}\right)\middle\|\pi''\left(\cdot\middle\vert\mathsfit{S}\right)\right)\right]$


## 第428页倒数第2组通栏数学表达式

$\sum\limits_ {\left(\mathsfit{S},\mathsfit{A}\right)\in\mathcal{D}}h\left(\mathsfit{A}\middle\vert\mathsfit{S};\boldsymbol\theta\right)-\mathop{\mathrm{logsumexp}}\limits_ {\mathsfit{a}\in\mathcal{A}\left(\mathsfit{S}\right)}h\left(\mathsfit{a}\middle\vert\mathsfit{S};\boldsymbol\theta\right)$

#### 改为

$\sum\limits_ {\left(\mathsfit{S},\mathsfit{A}\right)\in\mathcal{D}}\left(h\left(\mathsfit{S},\mathsfit{A};\boldsymbol\theta\right)-\mathop{\mathrm{logsumexp}}\limits_ {\mathsfit{a}\in\mathcal{A}\left(\mathsfit{S}\right)}h\left(\mathsfit{S},\mathsfit{a};\boldsymbol\theta\right)\right)$


## 第431页算法15-1第2.2.2步（共2处）

$\psi$

#### 改为

$\phi$


## 第450页最后2行

$=\sum\limits_ {\mathsfit{s'},\tilde r}{\tilde p\left(\mathsfit{s'},\tilde r\middle\vert\mathsfit{s},\mathsfit{a}\right)\left[\tilde r+\gamma{\tilde v}_ \pi\left(\mathsfit{s'}\right)\right]}$

$=\sum\limits_ {\mathsfit{s'},r}{p\left(\mathsfit{s'},r\middle\vert\mathsfit{s},\mathsfit{a}\right)\left[r-{\bar r}_ \pi+\gamma{\tilde v}_ \pi\left(\mathsfit{s'}\right)\right]}$

#### 改为

$=\sum\limits_ {\mathsfit{s'},\tilde r}{\tilde p\left(\mathsfit{s'},\tilde r\middle\vert\mathsfit{s},\mathsfit{a}\right)\left[\tilde r+{\tilde v}_ \pi\left(\mathsfit{s'}\right)\right]}$

$=\sum\limits_ {\mathsfit{s'},r}{p\left(\mathsfit{s'},r\middle\vert\mathsfit{s},\mathsfit{a}\right)\left[r-{\bar r}_ \pi+{\tilde v}_ \pi\left(\mathsfit{s'}\right)\right]}$


## 第451页第2组通栏数学表达式第1行

$\sum\limits_{\mathsfit{s}',r}{\tilde{p}\left(\mathsfit{s}',\tilde{r}\middle\vert\mathsfit{s},\mathsfit{a}\right)}$

#### 改为

$\sum\limits_{\mathsfit{s}',\tilde{r}}{\tilde{p}\left(\mathsfit{s}',\tilde{r}\middle\vert\mathsfit{s},\mathsfit{a}\right)}$


## 第451页第4组通栏数学表达式第2行

$\sum\limits_{\mathsfit{s}'}p_ \pi\left(\mathsfit{s'}\middle\vert\mathsfit{s},\mathsfit{a}\right)$

#### 改为
 
$\sum\limits_{\mathsfit{s}',\mathsfit{a}'}p_ \pi\left(\mathsfit{s'},\mathsfit{a}'\middle\vert\mathsfit{s},\mathsfit{a}\right)$


## 第453页第4组通栏数学表达式

状态价值： $\bar{v}_ \ast\left(\mathsfit{s}\right)=\sup_ \pi{\bar{v}_ \pi^{\left(\gamma\right)}}\left(\mathsfit{s}\right),\quad\mathsfit{s}\in\mathcal{S}$ ,

动作价值： $\bar{q}_ \ast\left(\mathsfit{s},\mathsfit{a}\right)=\sup_ \pi{\bar{q}_ \pi^{\left(\gamma\right)}}\left(\mathsfit{s},\mathsfit{a}\right),\quad\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}$ 。

#### 改为

状态价值： $\bar{v}_ \ast\left(\mathsfit{s}\right)=\sup_ \pi{\bar{v}_ \pi\left(\mathsfit{s}\right)},\quad\mathsfit{s}\in\mathcal{S}$ ,

动作价值： $\bar{q}_ \ast\left(\mathsfit{s},\mathsfit{a}\right)=\sup_ \pi{\bar{q}_ \pi\left(\mathsfit{s},\mathsfit{a}\right)},\quad\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}$ 。


## 第454页倒数第3行

$\tilde{q}_ \pi\left(\mathsfit{S}_ {t+1},\mathsfit{A}_ {t+1}\right)\left(1-D'\right)$

#### 改为

$\tilde{q}_ \pi\left(\mathsfit{S}_ {t+1},\mathsfit{A}_ {t+1}\right)\left(1-D_ {t+1}\right)$


## 第454页最后1组通栏数学表达式

$\tilde{q}\left(\mathsfit{S},\mathsfit{A}\right)$

#### 改为

$\tilde{q}\left(\mathsfit{S},\mathsfit{A};\mathbfit{w}\right)$


## 第455页算法16-1第2.2.6步第2行

$\nabla q\left(\mathsfit{S},\mathsfit{A},\mathbfit{w}\right)$

#### 改为

$\nabla\tilde{q}\left(\mathsfit{S},\mathsfit{A},\mathbfit{w}\right)$


## 第456页算法16-2第2.2.4步第1行和第3行（共2处）

#### 删去

$\gamma$


## 第462页第2组通栏数学表达式（1处）和第4组通栏数学表达式（2处）共3处

$\frac1h\sum\limits_ {0<\tau\leqslant h}{\gamma^\tau R_ {t+\tau}}$

#### 改为

$\frac1h\sum\limits_ {0<\tau\leqslant h}{R_ {t+\tau}}$


## 第464页第3组通栏数学表达式第1行

$\left({\huge\tau},\mathsfit{s},r\middle\vert\mathsfit{s},\mathsfit{a}\right)=\Pr\left[{\huge\tau}_ i={\huge\tau},\right.$

#### 改为

$\left(\tau,\mathsfit{s}',r\middle\vert\mathsfit{s},\mathsfit{a}\right)=\Pr\left[{\huge\tau}_ i=\tau,\right.$


## 第464页第3组通栏数学表达式第2行

${\huge\tau}\in\mathcal{T}$

#### 改为

$\tau\in\mathcal{T}$


## 第465页最后1组通栏数学表达式

状态分布: $\bar\rho_ \pi\left(\mathsfit{s}\right)=\lim\limits_ {h\rightarrow+\infty}{\mathrm{E}_ \pi\left[\frac1h\sum\limits_ {0\leqslant t < h}{\gamma^t1_ {\left[\mathsfit{S}_ t=\mathsfit{s}\right]}}\right]},\quad\mathsfit{s}\in\mathcal{S}$ ，

状态动作对分布: $\bar\rho_ \pi\left(\mathsfit{s},\mathsfit{a}\right)=\lim\limits_ {h\rightarrow+\infty}{\mathrm{E}_ \pi\left[\frac1h\sum\limits_ {0\leqslant t < h}{\gamma^t1_ {\left[\mathsfit{S}_ t=\mathsfit{s},\mathsfit{A}_ t=\mathsfit{a}\right]}}\right]},\quad\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}$ 。

#### 改为

状态分布: $\bar\rho_ \pi\left(\mathsfit{s}\right)=\lim\limits_ {h\rightarrow+\infty}{\mathrm{E}_ \pi\left[\frac1h\sum\limits_ {0\leqslant t < h}{1_ {\left[\mathsfit{S}_ t=\mathsfit{s}\right]}}\right]},\quad\mathsfit{s}\in\mathcal{S}$ ，

状态动作对分布: $\bar\rho_ \pi\left(\mathsfit{s},\mathsfit{a}\right)=\lim\limits_ {h\rightarrow+\infty}{\mathrm{E}_ \pi\left[\frac1h\sum\limits_ {0\leqslant t < h}{1_ {\left[\mathsfit{S}_ t=\mathsfit{s},\mathsfit{A}_ t=\mathsfit{a}\right]}}\right]},\quad\mathsfit{s}\in\mathcal{S},\mathsfit{a}\in\mathcal{A}$ 。


## 第466页第1组通栏数学表达式

$\gamma^{{\huge\tau}_ t}$

#### 改为

$\gamma^{{\huge\tau}_ i}$


## 第466页第3个通栏数学表达式第2行和第5个通栏数学表达式第2行（共2处）

$\left[r+\right.$

#### 中的 $r$ 上面加圆括号


## 第472页第10行

$b'=u\left(b,\mathsfit{a},\mathsfit{o}\right)$

#### 改为

$b'=\mathfrak{u}\left(b,\mathsfit{a},\mathsfit{o}\right)$


## 第472页表16-5表头文字

$\omega\left(\mathsfit{r},\mathsfit{s'},\mathsfit{o}\middle\vert b,\mathsfit{a}\right)$

#### 改为

$\omega\left(r,\mathsfit{s'},\mathsfit{o}\middle\vert b,\mathsfit{a}\right)$


## 第475页表格16-8中间那列

| 动作 $\mathsfit{a}$ |
| ---- |
| $\mathsfit{a}_ \text{听}$ |
| $\mathsfit{a}_ \text{听}$ |
| $\mathsfit{a}_ \text{听}$ |

#### 改为

| 动作 $\mathsfit{a}$ |
| ---- |
| $\mathsfit{a}_ \text{左}$ |
| $\mathsfit{a}_ \text{右}$ |
| $\mathsfit{a}_ \text{听}$ |


## 第477页第1个通栏数学表达式

$q_ \pi\left(b,\mathsfit{a}\right)=r\left(b,\mathsfit{a}\right)+\gamma\sum\limits_ \mathsfit{o}{\omega\left(\mathsfit{o}\middle\vert b,\mathsfit{a}\right)v_ \pi\left(u\left(b,\mathsfit{a},\mathsfit{o}\right)\right)}$

#### 改为

$q_ \pi\left(b,\mathsfit{a}\right)=r\left(b,\mathsfit{a}\right)+\gamma\sum\limits_ \mathsfit{o}{\omega\left(\mathsfit{o}\middle\vert b,\mathsfit{a}\right)v_ \pi\left(\mathfrak{u}\left(b,\mathsfit{a},\mathsfit{o}\right)\right)}$


## 第480页倒数第2个通栏数学表达式

$\prod\limits_{\tau'=\tau}^{t-1}$

#### 改为

$\prod\limits_{\tau'=t}^{\tau-1}$


## 第480页倒数第1个通栏数学表达式

$\sum\limits_{\tau=0}^{t_ \text{max}-1}$

#### 改为

$\sum\limits_{\tau=0}^{t_ \text{max}-t-1}$


## 第481页第1组通栏数学表达式

把其中的 $\mathsfit{s}$ 改为 $\mathsfit{x}$ （共7处），把其中的 $\mathcal{S}$ 改为 $\mathcal{X}$ （共2处）。


## 第489页第3行

信任状态是

#### 改为

信任状态价值是
