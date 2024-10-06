# 搭建开发环境

本文介绍如何在macOS （含M芯片版）上搭建开发环境。

## 第1部分：最小安装

本部分介绍搭建最小环境的方法。完成本步后，你可以运行第1-5章、第13章、第16章代码。

#### 安装Anaconda 3

**步骤：**

- 从https://www.anaconda.com/products/distribution 下载Anaconda 3安装包（选择MacOS Graphical版的安装包）。安装包名字像 `Anaconda3-2024.06-1-MacOSX-x86_64.pkg`（M芯片版安装包名字像`Anaconda3-2024.06-1-MacOSX-amd64.pkg`），大小约0.7 GB。
- 双击安装包启动安装向导完成安装。需要安装在剩余空间大于13GB的硬盘上。（如果空间小于这个数，虽然也能完成Anaconda 3的安装，但是后续步骤的空间就不够了。13GB是后续所有步骤需要的空间。）安装过程中记下Anaconda的安装路径。默认路径为：`/opt/anaconda3`。后续操作会用到这个路径。

#### 新建conda环境

本步非必须，但是强烈推荐您执行本步骤。

**步骤：**

- 运行“终端”，执行下列命令：（其中`py311`是conda环境名， 你也可以取其他名称）
   ```
   conda create --name py311 python=3.11
   conda activate py311
   ```
- 在新的conda目标环境中可以用下列命令安装jupyter:
   ```
   conda install jupyter
   ```

#### 安装Python扩展包：numpy、pandas等

**步骤：**

- 在目标conda环境中（你可以在终端中用`conda activate py311`进入名为`py311`的conda环境）执行下列命令：
   ```
   conda install numpy pandas scipy sympy matplotlib
   ```

#### 安装`gym[classic_control]`、`gym[toy_text]`、 `gym[atari]`

**步骤：**

- 在目标conda环境中执行下列命令：
   ```
   pip install --upgrade 'gym[classic_control,toy_text,atari,accept-rom-license,other]'
   ```

#### 运行Jupyter Notebook

**步骤：**

- 确认Anaconda的安装路径。默认路径为：`/opt/anaconda3`。
- 选择代码的根目录。比如，我可以选择`~/Documents/Anaconda`。（如果目录事先不存在，可以先创建它。）
- 改变目录为代码的根目录：
   ```
   C:
   cd C:%HOMEPATH%\Documents\Anaconda
   ```
- 运行下列代码（用到了conda环境名，例如`py311`）：
   ```
   /opt/anaconda3/envs/py311/bin/jupyter-notebook
   ```

- 等待默认浏览器弹出。推荐您使用Chrome作为默认浏览器。

## 第2部分：安装TensorFlow和PyTorch

本部分介绍TensorFlow和PyTorch的安装。书中第6-10章、第12章、第14章、第15章需要使用TensorFlow和PyTorch。安装需要基于第1部分已经安装好的环境。完成本部分后，你可以运行第1-9章、第13章和第16章的代码。

请在App Store里安装Xcode。

本书涉及TensorFlow或PyTorch的代码都提供了TensorFlow和PyTorch的1:1对照版本。你可以只学习其中一种，也可以两种都学习。如果您在纠结于学哪一种，那建议您两种都学。

本书代码只需要CPU版本的TensorFlow和PyTorch。当然您也可以用更快更强的GPU版本。

#### 在conda环境中安装TensorFlow

**步骤：**

- 安装TensorFlow（CPU版）和TensorFlow probability：在目标conda环境中执行下列命令
   ```
   pip install --upgrade tensorflow-macos tensorflow_probability
   ```

#### 在conda环境中安装PyTorch

**步骤：**

- 安装PyTorch（CPU版）：在目标conda环境中执行下列命令
   ```
   conda install pytorch cpuonly -c pytorch
   ```

## 第3.1部分：安装`gym[box2d]`

第10-11章代码需要用到`gym[box2d]`，这个部分安装`gym[box2d]`。如果您不想看这两章代码，可以略过此步，不影响其他部分。

该安装需要基于第2部分装好的环境。完成此步后可以运行第1-13章和第16章代码。

请从App Store里安装Xcode。

#### 安装SWIG

**步骤：**

- 在conda环境外执行下列命令（可以用`conda deactivate`退出conda环境）：
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   （中国内地用户如果遇到网络链接困难，可以先去 `https://github.com/Homebrew/install`下载文件`install.sh`并执行它：`/bin/bash -c ./install.sh`。）然后为Homebrew添加路径：
   ```
   echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /Users/apple/.zprofile
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/apple/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```
- 用Homebrew安装SWIG：
   ```
   brew install swig
   ```


#### 在conda环境中安装`gym[box2d]`

**步骤：**

- 在目标conda环境中执行下列命令：
   ```
   pip install --upgrade 'gym[box2d]'
   ```

## 第3.2部分：安装boardgame2

`boardgame2` 是第14章将开发的环境。第14章会介绍如何一步步开发这个环境。当然也可有开发好的现成版本，可以用下列步骤安装。如果您不想看这章代码，可以略过此步，不影响其他部分。

该安装需要基于第2部分装好的环境。

**步骤：**

- 在目标conda环境中执行下列命令以安装`boardgame2`：
   ```
   pip install --upgrade pybullet
   ```

## 第3.3部分：安装PyBullet

第15章代码需要PyBullet，本部分安装PyBullet。如果您不想看这章代码，可以略过此步，不影响其他部分。

由于PyBullet需要用到旧版的Gym，所以最好为PyBullet单独建一个环境，以免污染现有环境。

**步骤：**

- 新建Anaconda环境。

- 在新Anaconda环境里安装Gym等。

- 在目标conda环境中执行下列命令：
   ```
   pip install --upgrade pybullet
   ```
