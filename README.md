
- [blah]()
- [Home Installation Instructions](#home-installation-instructions)

## Home Installation Instructions
The following software will be required for the course.
- [Command line](#command-line) ([Linux](#linux), [Mac](#mac), [Windows](#windows))
- [Python](#python) ([Linux](#linux-1), [Mac](#mac-1), [Windows](#windows-1))
- [Git](#git) ([Linux](#linux-2), [Mac](#mac-2), [Windows](#windows-2))
- [VS Code](#vs-code) ([Linux](#linux-3), [Mac](#mac-3), [Windows](#windows-3))

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Command line
### Linux
### Mac
For those of you wanting to install the `tree` program at home try the following.
Install HomeBrew
```sh
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Install tree
```sh
$ brew install tree
```
### Windows
You need to download [GitBash](https://gitforwindows.org/) to have a linux-style command-line.

## Python
**Required software**:
- Python 3.8+
    - [arcade](http://arcade.academy)
    - pytest
    - pycodestyle
    - mypy

### Install Python Packages
Once you have Python installed, you should have pip installed too. Install the python packages required for the course:
```sh
pip install arcade pycodestyle mypy pytest
```

### Linux
In the terminal enter the following commands.
```sh
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
curl https://bootstrap.pypa.io/3.2/get-pip.py | python3.8
```
### Mac
Try the instructions above for Linux. Please let me know if it doesn't work.
### Windows
Get the `Windows x86-64 executable installer` from the [Python downloads](https://www.python.org/downloads/release/python-381) page.
Follow directions from [Corey's tutorial video](http://www.youtube.com/watch?v=YYXdXT2l-Gg&t=5m44s).

## Git
### Linux
```sh
sudo apt-get install git
```
### Mac
### Windows
You need to download [GitBash](https://gitforwindows.org/) to have a linux-style command-line.

## VS Code
Visit the [VS Code Download](https://code.visualstudio.com/download) page.
### Linux
### Mac
### Windows
