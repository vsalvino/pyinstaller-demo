PyInstaller Demo
================

First we will make a simple python command line tool, then package it up into an `.exe`
using PyInstaller.


Environment Set Up
------------------

First, create a virtual environment (Python 3.7) as so:
```
python -m venv ~/Envs/pyinstaller-demo
```

Now activate it:
```
# Mac/Linux
source ~/Envs/pyinstaller-demo/bin/activate

# Windows (PowerShell)
~/Envs/pyinstaller-demo/Scripts/Activate.ps1
```


Part 1: Basic Utility
---------------------

In `util.py` we have a function `list_files` that will simply produce a list of files
in a given directory.


Part 2: Call our function
-------------------------

Now, in order to run our function from the command line, we need a Python script to
call our function. See `main.py`. To run `main.py`:

```
python main.py
```

This works great, except that the directory is hard-coded in `main.py`. If we want to
interact with it, we need to make a more robust command line interface.


Part 3: A Real Command Line Interface
-------------------------------------

Now, in `cli.py`, we are going to use `argparse` to create a simple command line
interface that can accept the path we want as input.

To run the CLI:

```
python cli.py --help
python cli.py <enter a path>
```

Voila!


Part 4: Build an `.exe` with PyInstaller
----------------------------------------

To distribute our app to user who do not already have python installed, first we
must build:

```
pip install pyinstaller
```

Now build:

```
pyinstaller cli.py --name "myapp" --clean --onedir
```

That will create a directory containing all the dependencies and an executable.

To build it as a single executable (which runs slower, but is more convenient to
distribute), use the `--onefile` option:

```
pyinstaller cli.py --name "myapp" --clean --onefile
```
