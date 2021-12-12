# 自动驾驶 AirSimNH

很抱歉，这个例子不再支持 AirSimNH 1.6.0 以上版本。

AirSim最新版和Jupyter Notebook不再兼容。原因：AirSim依赖的包msgpack-rpc-python进一步依赖tornado的旧版本（tornado<5），但是Jupyter Notebook要求更高版本的tornado，两者不能共存。


现在要想用airsim，就不能用Jupyter Notebook。在Anaconda中，可以新建一个不带Jupyter Notebook的环境专门来运行airsim。

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

目前参数不再适合 AirSimNH 1.6.0 以上版本。
