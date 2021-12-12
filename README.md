# 🎓 InCollege CLI 🎓

This repository is created for purposes of collaboration between students for a Software Engineering class (CEN4020F21) at the University of South Florida in Tampa, FL. MIT license is implied. Code is free and open for everyone.

## Overview

Hello and welcome to one-stop-shop for all career resources you'll need as a student. You can use this InCollege Command Line Interface (InCollege CLI) to:
1. Find friends.
2. Look for jobs.
3. Learn relevant skills.
4. And more...

## Architecture

Architecture and design are important, however, we are still developing our project. Below you can see a snapshot of our application depicted as a state diagram. When it comes to code, we have a driver function implemented in main `in_college.py` file, and a utility file `utils.py` with all the data/content and verification procedures. Very simple, functional, works. We also use a lot of emojis.

![alt text](https://github.com/USFCEN4020/CEN4020F21TeamWyoming/blob/main/media/UI%20Logic.png)

## Running and contributing

1. Clone the repository.

Either through git or using GitHub CLI:

```shell
git clone https://github.com/USFCEN4020/CEN4020F21TeamWyoming.git
gh repo clone USFCEN4020/CEN4020F21TeamWyoming # GitHub CLI.
```

2. Initialize virtual environment.

```shell
python3 -m pip install --user virtualenv # install venv.
python3 -m venv venv # initialize environment with name venv.
```

And then enter the virtual environment to install packages:

```shell
source venv/bin/activate # linux
. \venv\Scripts\activate # windows

pip install -r requirements.txt # to install packages.
```

Finally, run the program:

```shell
cd src/
python3 in_college.py
```

To contribute, follow coding standards and submit a PR 🚀.

## Standards

Coding standards are followed from this industry accepted guide: [link](https://google.github.io/styleguide/pyguide.html).

To summarize general rules:
* Function, files, variables are snake-case: `long_number_a = get_my_number(4)`
* Limit line width to 80 characters.
* Docstrings should be included with every function.

And you're good to go.

