# 搭建开发环境

本文介绍如何在Windows 10或11电脑上搭建开发环境。

## 第1部分：最小安装

本部分介绍搭建最小环境的方法。完成本步后，你可以运行第1-5章、第13章、第16章代码。

#### 安装Anaconda 3

**步骤：**

- 从https://www.anaconda.com/products/distribution 下载Anaconda 3安装包（选择Windows版的安装包）。安装包名字像 `Anaconda3-2024.06-1-Windows-x86_64.exe`，大小约0.9GB。
- 双击安装包启动安装向导完成安装。需要安装在剩余空间大于13GB的硬盘上。（如果空间小于这个数，虽然也能完成Anaconda 3的安装，但是后续步骤的空间就不够了。13GB是后续所有步骤（除了安装Visual Studio以外）需要的空间。）安装过程中记下Anaconda的安装路径。默认路径为：`C:%HOMEPATH%\anaconda3`。后续操作会用到这个路径。

#### 新建conda环境

本步非必须，但是强烈推荐您执行本步骤。

**步骤：**

- 以管理员身份运行Anaconda Prompt，执行下列命令：（其中`py311`是conda环境名， 你也可以取其他名称）
   ```
   conda create --name py311 python=3.11
   conda activate py311
   ```

#### 安装Python扩展包：numpy、pandas等

**步骤：**

- 以管理员身份运行Anaconda Prompt，在目标conda环境中（你可以用`conda activate py311`进入名为`py311`的conda环境）执行下列命令：
   ```
   conda install numpy pandas scipy sympy matplotlib
   ```

#### 安装`gym[classic_control]`、`gym[toy_text]`、 `gym[atari]`

**步骤：**

- 以管理员身份运行Anaconda Prompt，在目标conda环境中执行下列命令：
   ```
   pip install --upgrade gym[classic_control,toy_text,atari,accept-rom-license,other]
   ```

#### 运行Jupyter Notebook

**步骤：**

- 确认Anaconda的安装路径。默认路径为：`C:%HOMEPATH%\anaconda3`。
- 选择代码的根目录。比如，我可以选择`C:%HOMEPATH%\Documents\Anaconda`。
- 打开命令提示符（不是Anaconda Prompt），改变目录为代码的根目录：
   ```
   C:
   cd C:%HOMEPATH%\Documents\Anaconda
   ```
- 运行下列代码（用到了conda环境名，例如`py311`）：
   ```
   C:%HOMEPATH%\anaconda3\python.exe C:%HOMEPATH%\anaconda3\cwp.py C:%HOMEPATH%\anaconda3\envs\py311 C:%HOMEPATH%\anaconda3\envs\py311\python.exe C:%HOMEPATH%\anaconda3\Scripts\jupyter-notebook-script.py C:%HOMEPATH%\Documents\Anaconda
   ```

- 等待默认浏览器弹出。推荐您使用Chrome作为默认浏览器。

## 第2部分：安装TensorFlow和PyTorch

本部分介绍TensorFlow和PyTorch的安装。书中第6-10章、第12章、第14章、第15章需要使用TensorFlow和PyTorch。安装需要基于第1部分已经安装好的环境。完成本部分后，你可以运行第1-9章、第13章和第16章的代码。

#### 安装Visual Studio

TensorFlow和PyTorch都需要Visual Studio运行时。我们并不需要Visual Studio的图形界面，我们只需要运行时。

Visual Studio社区版是免费的，而且够用。装社区版就好了。

如果您的电脑上有老版本的Visual Studio，推荐先卸载老版本然后装最新版。

**步骤：**

- 访问`https://visualstudio.microsoft.com/downloads/`下载Visual Studio社区版安装包。
- 双击运行安装想到完成安装。具体安装什么组件不太重要，因为我们需要的核心功能肯定是会安装的。在C盘需要8GB的空间。如果你还想装别的组件，可以选择其他盘，选的组件越多占用空间越多，比如15GB。

#### 在conda环境中安装TensorFlow和PyTorch

本书涉及TensorFlow或PyTorch的代码都提供了TensorFlow和PyTorch的1:1对照版本。你可以只学习其中一种，也可以两种都学习。如果您在纠结于学哪一种，那建议您两种都学。

本书代码只需要CPU版本的TensorFlow和PyTorch。当然您也可以用更快更强的GPU版本。

请在运行下列步骤前确保最新版本的Visual Studio已经成功安装。否则，看似也可以装好TensorFlow和PyTorch，实际上是不能用的。

**步骤：**（CPU版）

- 安装TensorFlow和TensorFlow probability：以管理员身份运行Anaconda Prompt，在目标conda环境中执行下列命令
   ```
   pip install --upgrade tensorflow tensorflow_probability
   ```
   
- 安装PyTorch：以管理员身份运行Anaconda Prompt，在目标conda环境中执行下列命令
   ```
   conda install pytorch cpuonly -c pytorch
   ```

## 第3.1部分：安装`gym[box2d]`

第10-11章代码需要用到`gym[box2d]`，这个部分安装`gym[box2d]`。如果您不想看这两章代码，可以略过此步，不影响其他部分。

该安装需要基于第2部分装好的环境。完成此步后可以运行第1-13章和第16章代码。完成了全部的第3.1-3.3部分后可以运行所有章节的代码。

#### 安装SWIG

**步骤：**

- 访问`http://www.swig.org/download.html`下载SWIG安装包。安装包的URL可能为
  http://prdownloads.sourceforge.net/swig/swigwin-4.1.1.zip，大小约11MB。
- 将安装包解压到永久位置，例如`%PROGRAMFILE%\swig` （该位置需要管理员权限）。
- 将解压后得到的文件中`swig.exe`所在的目录（如`%PROGRAMFILE%\swig\swigwin-4.1.1`）加到系统环境变量`PATH`中。（添加环境变量的方法是：用Windows+R打开“运行”窗口，输入`sysdm.cpl`并回车打开“系统属性”。然后在“高级”选项卡下找到“环境变量”，找到`PATH`并设置。
- 重启电脑确保环境变量生效。

#### 在conda环境中安装`gym[box2d]`

**步骤：**

- 以管理员身份运行Anaconda Prompt，在目标conda环境中执行下列命令：
   ```
   pip install --upgrade gym[box2d]
   ```

## 第3.2部分：安装boardgame2

`boardgame2` 是第14章将开发的环境。第14章会介绍如何一步步开发这个环境。当然也可有开发好的现成版本，可以用下列步骤安装。如果您不想看这章代码，可以略过此步，不影响其他部分。

该安装需要基于第2部分装好的环境。

**步骤：**

- 以管理员身份运行Anaconda Prompt，在目标conda环境中执行下列命令以安装`boardgame2`：
   ```
   pip install --upgrade pybullet
   ```

## 第3.3部分：安装PyBullet

第15章代码需要PyBullet，本部分安装PyBullet。如果您不想看这章代码，可以略过此步，不影响其他部分。

由于PyBullet需要用到旧版的Gym，所以最好为PyBullet单独建一个环境，以免污染现有环境。

**步骤：**

- 新建Anaconda环境。

- 在新Anaconda环境里安装Gym等。

- 以管理员身份运行Anaconda Prompt，在目标conda环境中执行下列命令：
   ```
   pip install --upgrade pybullet
   ```
