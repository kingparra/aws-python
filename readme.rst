************
 aws-python
************


Overview
--------
This repo contains programming exercises and notes for the Yellow Tail Tech!
Python Automation winter 2024 class.

This course covers python programming basics and how to automate tasks on AWS
using the SDK. There will also be a lab on interacting with CheckMK using Python.

Lab 5 will require some infrastructure set up beforehand (two servers and a vpc).
You can find automation for that in `kingparra/aws-python-lab-setup-tf
<https://github.com/kingparra/aws-python-lab-setup-tf>`_.


How to interact with the code
-----------------------------
Projects are managed using `devbox <https://www.jetpack.io/devbox/>`_
and `poetry <https://python-poetry.org/>`_. You can use these instructions
to interact with the code.

* Move to the project directory::

    cd $project-name

* Install devbox and enter a shell to get the specified version of python and poetry (optional)::

    devbox shell
    # ...system-level packages will be installed...

* Use poetry to install python libraries (listed in ``pyproject.toml``) into a managed venv::

     poetry install

* Run the entry point to the program in the venv managed by poetry::

     poetry run $project-name

* Run the test suite in the venv::

     poetry run pytest

* Generate a VS Code devcontainer and launch your editor to get LSP completion::

     devbox generate devcontainer
     code .


Suggesting improvements
-----------------------
If you have a suggestion to improve the code, please file an issue or use the
discussions tab. You can link to specific lines in the code from discussions.
If you want to contribute code, make a fork of the repo and submit a pull request.

