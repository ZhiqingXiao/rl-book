# Set Up Developing Environment

This article introduces how to set up developing environment in a macOS (w/o or w/ M chip).

This setup requires the Internet connection.

## Part 1: Minimum Installation

This part will show how to set up a minimum environment. After this step, you are able to run codes in Chapter 1-5, 13, 15.

#### Install Anaconda 3

**Steps:**

- Download the installer on https://www.anaconda.com/products/distribution (Pick MacOS Graphical Installer for MacOS users). The name of installer is alike `Anaconda3-2024.10-1-MacOSX-x86_64.pkg` (or `Anaconda3-2024.10-1-MacOSX-amd64.pkg` for M chip), and the size is about 0.7 GB.
- Double click the installer to start the install wizard and install accordingly. The free space of the disk should be at least 13GB. (If the free space of the disk is too little, you may still be able to install Anaconda 3 itself, but you may not have enough free space in the follow-up steps. 13GB is the storage requirements for all steps in this article.) Record the location of Anaconda installation. The default location is `/opt/anaconda3`. We will use the location in the sequal.

#### Create a New Conda Environment

This step is strongly recommended but not compulsory.

**Steps:**

- Launch "Terminal", and execute the following commands: (where `py310` is the conda environment name, and you can change it to an other name.) (Remark: Here we use Python 3.10 rather than Python 3.11 or Python 3.12 or Python 3.13, it is because the latest version of `gym[toy_text,classic_control,box2d]` depends on `pygame==2.1`, but `pygame==2.1` is not compatible with Python 3.12, although the latest version of `pygame` supports Python 3.12. Resolving the compatible between the latest version of Gym and Python 3.11&3.12&3.13 needs some efforts. For simplify, this guide uses Python 3.10.)
   ```
   conda create --name py310 python=3.10
   conda activate py310
   ```

- In the new environment you may need to install jupyter:
   ```
   conda install jupyter
   ```

#### Install Packages: Numpy, Pandas, etc

**Steps:**

- In the terminal, execute the following commands in the target conda environment:
   ```
   conda install numpy pandas scipy sympy matplotlib
   ```

#### Install `gym[classic_control]`, `gym[toy_text]`, and `gym[atari]`

**Steps:**

- Execute the following commands in the target conda environment (you can use `conda activate py310` to go to the conda environment `py310`):
   ```
   pip install --upgrade 'gym[classic_control,toy_text,atari,accept-rom-license,other]'
   ```

#### Launch Jupyter Notebook

**Steps:**

- Check the location of Anaconda installation. The default location is `/opt/anaconda3`.
- Choose a directory as the root directory to save the codes. For example, I choose `~/Documents/Anaconda`. (If the folder does not exist, you may need to create it first.)
- Go to the root of the notebooks:
   ```
   cd ~/Documents/Anaconda
   ```
- Execute `python` with the information of the conda environment (say `py310`):
   ```
   /opt/anaconda3/envs/py310/bin/jupyter-notebook
   ```

- Wait for your default browser popping up. You are recommended to use Chrome.

## Part 2: Install TensorFlow and/or PyTorch

This part will show how to install TensorFlow and/or PyTorch upon the minimum environment in Part 1. Codes in Chapter 6-10, 12, 14, 16 need TensorFlow and/or PyTorch. After this step, you are able to run codes in Chapter 1-9, 13, 15.

Please install the latest version of Xcode from AppStore.

This book provides one-on-one mapping codes from TensorFlow and PyTorch. You can try both, or either of them. If you have difficulty in choosing between TensorFlow and PyTorch, try both of them.

This book only needs CPU version. You can of course install GPU versions, which may execute faster.

#### Install TensorFlow in Conda Environment

**Steps:**

- Install TensorFlow (CPU version) and TensorFlow probability: Execute the following command in the target conda environment:
   ```
   pip install --upgrade tensorflow-macos tensorflow_probability
   ```

#### Install PyTorch in Conda Environment

**Steps:**

- Install PyTorch (CPU version): Execute the following command in target conda environment:
   ```
   pip install --upgrade pytorch
   ```

## Part 3.1: Install `gym[box2d]`

Codes in Chapter 10-11 use `gym[box2d]`. You can skip this part if you do not care the codes in Chapter 10-11. It does not impact other parts.

This part will show how to install `gym[box2d]` upon the environment with PyTorch and/or TensorFlow in Part 2. Upon completed this part, you are able to run codes in Chapter 1-13, 15. If you complete all of Part 3.1-3.3, you are able to run codes in all chapters.

Please install the latest version of Xcode from AppStore.

#### Install SWIG

**Steps:**

- Install Homebrew outside Anaconda environment (We can use `conda deactivate` to quit the Anaconda environment.):
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   (Chinese mainland user: Go to https://github.com/Homebrew/install, download install.sh and execute it: `/bin/bash -c ./install.sh`.) Then add paths for Homebrew:
   ```
   echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /Users/apple/.zprofile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/apple/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
   ```
- Install SWIG using Homebrew:
   ```
   brew install swig
   ```

#### Install `gym[box2d]` in a Conda Environment

**Steps:**

- Execute the following command in target conda environment:
   ```
   pip install --upgrade 'gym[box2d]'
   ```

## Part 3.2: Install boardgame2

`boardgame2` is a package that will be developed in Chapter 14. Chapter 14 will guide you step-by-step on how to develop it. Nevertheless, there is an off-the-shelf package, too. You can skip this part if you do not care the codes in Chapter 14.

**Steps:**

- Execute the following command in the target conda environment to install `boardgame2`:
   ```
   pip install --upgrade boardgame2
   ```

## Part 3.3: Install PyBullet

Codes in Chapter 16 use PyBullet. You can skip this part if you do not care the codes in Chapter 16.

Since PyBullet depends on an old version of Gym, so it is better install it in a new conda environment so that it will not pollute current conda environment.

**Steps:**

- Create a new conda environment

- Install packages such as Gym in the new environment.

- Execute the following command in the target conda environment:
   ```
   pip install --upgrade pybullet
   ```
