# Empire Project Manager
Initiate and manages subsequent empire projects

For now, there's only one command: ``init``.

## Usage

1. Clone this repo
2. cd to the path you have cloned this repo in
3. ``pip install -r requirements.txt``. This will install the requirements for this program to work.
4. If you only have Python 3 installed: ``python empire.py init``
   1. Otherwise ``python3 empire.py init``
5. Questions will be asked in order to fill some variables to implement file templates and build proper paths

## Standards

### Project naming
Each **empire** project should be name: ``empire-<PROJECT-NAME>``:
* replace <PROJECT-NAME> by the-name-of-project
* each word must be separated by ``-``
* all letters must be lower cased

### In-code naming
By in-code naming, this is the project name used in code, so it must be parseable and importable by Python.
The standard is ``e<project_name>``:
* replace <project_name> by the_name_of_project
* all letters must be lower cased
* each word must be separated by ``_``

### Minimum Python version
The minimum Python version is *currently* ``3.10``. 

## Not so frequently asked question (who ask these questions anyways...)

* How to use type aliases in Python Sphinx?:
  * You should start the Python code file with ``from __future__ import annotations`` and add the alias to the ``conf.py`` (check at the bottom of the file, there's already one there)
* Remove a Cython module from making pylint explode?:
  * In ``pyproject.toml``, section ``[tool.pylint.main]``, add the following: ``extension-pkg-allow-list = ["package.name"]``  

## References

Python classifiers can be found here: https://pypi.org/classifiers/