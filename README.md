#  Reddit Username Checker
## Credit

  Original source for this came from [here](https://youtu.be/96EBlrKOpH4), the authour is [c0rtepentest](https://twitter.com/c0rtepentest).
  
  Code has been used from the [cli-checker](https://github.com/crock/cli-checker) and this guide is based off its [installation](https://github.com/crock/cli-checker/wiki/Installation), big thanks to [Crock](https://github.com/crock).
  
## Python Install

  Well first off you need the right `python 3+` [installer](https://www.python.org/downloads/) given it is only compatible with that.
  
  ![Python Install](https://i.imgur.com/xw0RAb0.png)
  
  Make sure to have `Add to PATH` otherwise there will be problems.
## Installation

1. Download the zip or clone the repository with Git onto your machine.
2. Install the dependencies using the the following command inside Command Prompt (Windows) or Terminal (Mac). If you use Python.exe, it will not work.

```
python -m pip install configparser requests
```

3. Edit the `config.ini` inside a text editor. It explains what to do inside of it.
4. Open Command Prompt or Terminal. We need to make it know where to find the checker files and so type:

```
cd *path to the folder*
```

5. Run the script via command line using the following command:

```
python reddit.py
```

If you need help please join this [discord](https://discord.gg/hpbQayV) for free support :)
