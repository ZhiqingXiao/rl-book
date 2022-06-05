# 自动驾驶 AirSimNH


2022年更新：AirSim最新版和Jupyter Notebook不再兼容。
- 原因：AirSim依赖的包msgpack-rpc-python进一步依赖tornado的旧版本（tornado<5），但是Jupyter Notebook要求更高版本的tornado，两者不能共存。
- 现在要想用airsim，就不能用Jupyter Notebook。在Anaconda中，可以新建一个不带Jupyter Notebook的环境专门来运行airsim。

```
conda update conda -n base

conda create -n airsim
conda activate airsim
conda install pip
conda install pandas
pip install --upgrade tensorflow
pip install --upgrade gym
pip install --upgrade airsim

python AirSimNH_tf.py
```

2022年更新：由于其他依赖库的更新，参数已经不能用了。目前作者没有重新提供参数的计划。
