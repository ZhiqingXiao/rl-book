# Set Up Developing Environment

This article introduces how to set up developing environment in a Windows 10/11 PC.

## Part 1: Minimum Installation

This part will show how to set up a minimum environment. After this step, you are able to run codes in Chapter 1-5, 13, 16.

#### Install Anaconda 3

**Steps:**

- Download the installer on https://www.anaconda.com/products/distribution (Pick Windows version for Windows users).The name of installer is alike `Anaconda3-2023.09-0-Windows-x86_64.exe`, and the size is about 0.9 GB.
- Double click the installer to start the install wizard and install accordingly. The free space of the disk should be at least 13GB. (If the free space of the disk is too little, you may still be able to install Anaconda 3 itself, but you may not have enough free space in the follow-up steps. 13GB is the storage requirements for all steps in this article except Visual Studio.) Record the location of Anaconda installation. The default location is `C:%HOMEPATH%\anaconda3`. We will use the location in the sequal.

#### Create a New Conda Environment

This step is strongly recommended but not compulsory.

**Steps:**

- Launch Anaconda Prompt as an Administrator, and execute the following commands: (where `py311` is the conda environment name, and you can change it to an other name.)
   ```
   conda create --name py311 python=3.11
   conda activate py311
   ```

#### Install Packages: Numpy, Pandas, etc

**Steps:**

- Launch Anaconda Prompt as an Administrator, and execute the following commands in the target conda environment:
   ```
   conda install numpy pandas scipy sympy matplotlib
   ```

#### Install `gym[classic_control]`, `gym[toy_text]`, and `gym[atari]`

**Steps:**

- In the target conda environment (you can use `conda activate py311` to go to the conda environment `py311`), execute the following commands in Anaconda Prompt as an Administrator:
   ```
   pip install --upgrade gym[classic_control,toy_text,atari,accept-rom-license,other]
   ```

#### Launch Jupyter Notebook

**Steps:**

- Check the location of Anaconda installation. The default location is `C:%HOMEPATH%\anaconda3`.
- Choose a directory as the root directory to save the codes. For example, I choose `C:%HOMEPATH%\Documents\Anaconda`.
- Open a Command Prompt (not Anaconda Prompt), and go to the root of the notebooks:
   ```
   C:
   cd C:%HOMEPATH%\Documents\Anaconda
   ```
- Execute `python.exe` with the information of the conda environment (say `py311`) (note that the following command has only one line):
   ```
   C:%HOMEPATH%\anaconda3\python.exe C:%HOMEPATH%\anaconda3\cwp.py C:%HOMEPATH%\anaconda3\envs\py311 C:%HOMEPATH%\anaconda3\envs\py311\python.exe C:%HOMEPATH%\anaconda3\Scripts\jupyter-notebook-script.py C:%HOMEPATH%\Documents\Anaconda
   ```

- Wait for your default browser popping up. You are recommended to use Chrome.

## Part 2: Install TensorFlow and/or PyTorch

This part will show how to install TensorFlow and/or PyTorch upon the minimum environment in Part 1. Codes in Chapter 6-10, 12, 14, 15 need TensorFlow and/or PyTorch. After this step, you are able to run codes in Chapter 1-9, 13, 16.

#### Install Visual Studio

Both TensorFlow and PyTorch require Visual Studio runtime. We will not use Visual Studio GUI - we just need its runtime.

Visual Studio Community version is free, and contains all we need.

If an older version of Visual Studio has been installed in your PC, you are recommended to uninstall it and then install the latest Visual Studio.

**Steps:**

- Download the installer of Visual Studio Community version on `https://visualstudio.microsoft.com/downloads/`.
- Execute the installer, and finish the installation following the wizard. What components to install does not matter, because the core components will always be installed. The storage requirements are about 8 GB in C disk (and more if you pick more components, may be as large as 15 GB, while some can be put in other disks).

#### Install TensorFlow and/or PyTorch in Conda Environment

This book provides one-on-one mapping codes from TensorFlow and PyTorch. You can try both, or either of them. If you have difficulty in choosing between TensorFlow and PyTorch, try both of them.

This book only needs CPU version. You can of course install GPU versions, which may execute faster.

Please install the latest version of Visual Studio before this step. Otherwise, the installation may seem to complete, but they actually do not work.

**Steps:** (CPU version)

- Install TensorFlow and TensorFlow probability: Execute the following commands in Anaconda Prompt as an Administrator:
   ```
   pip install --upgrade tensorflow tensorflow_probability
   ```
   
- Install PyTorch: Execute the following commands in Anaconda Prompt as an Administrator:
   ```
   conda install pytorch cpuonly -c pytorch
   ```

## Part 3.1: Install `gym[box2d]`

Codes in Chapter 10-11 use `gym[box2d]`. You can skip this part if you do not care the codes in Chapter 10-11. It does not impact other parts.

This part will show how to install `gym[box2d]` upon the environment with PyTorch and/or TensorFlow in Part 2. Upon completed this part, you are able to run codes in Chapter 1-13, 16. If you complete all of Part 3.1-3.3, you are able to run codes in all chapters.

#### Install SWIG

**Steps:**

- Get the installer of SWIG: http://www.swig.org/download.html. The URL of installer may be
  http://prdownloads.sourceforge.net/swig/swigwin-4.1.1.zip. The size of installer is about 11MB.
- Please unzip it into a permanent location, such as `%PROGRAMFILE%\swig` (this location requires administrator permission).
- Add the directory containing the unzipped file `swig.exe`, such as `%PROGRAMFILE%\swig\swigwin-4.1.1`, to the `PATH` of system variable. (The way to set environment variables is as follows: Press “Windows+R” to open the “Run” window, and then type `sysdm.cpl` and press Enter to open “System Properties”. Go to the “Advanced” Tab and click “Environment Variables”, and select `PATH` in it and add the location to it.
- Restart the PC to ensure that the change of system environment is in effect.

#### Install `gym[box2d]` in a Conda Environment

**Steps:**

- Execute the following command in Anaconda Prompt as an Administrator:
   ```
   pip install --upgrade gym[box2d]
   ```

## Part 3.2: Install boardgame2

`boardgame2` is a package that will be developed in Chapter 14. Chapter 14 will guide you step-by-step on how to develop it. Nevertheless, there is an off-the-shelf package, too. You can skip this part if you do not care the codes in Chapter 14.

**Steps:**

- Execute the following command in Anaconda Prompt as an Administrator to install `boardgame2`:
   ```
   pip install --upgrade pybullet
   ```

## Part 3.3: Install PyBullet

Codes in Chapter 15 use PyBullet. You can skip this part if you do not care the codes in Chapter 15.

Since PyBullet depends on an old version of Gym, so it is better install it in a new conda environment so that it will not pollute current conda environment.

**Steps:**

- Create a new conda environment

- Install packages such as Gym in the new environment.

- Execute the following command in the target conda environment:
   ```
   pip install --upgrade pybullet
   ```
