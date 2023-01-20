=============
PROJECT_NAME
=============

A project template which includes all setup for a Python 3.10 Data Science project

PROJECT_URL

Requirements
============
- python3.10
- pip
- pip-tools or conda


Installation
============
Create and activate your virtual environment.

Developers:

.. code-block:: bash

  scripts/setup-development.sh

Users:

.. code-block:: bash

  pip install . -r requirements.txt -c constraints.txt

Dependency Management
=====================

This project uses `pip-tools <https://github.com/jazzband/pip-tools>`_ for hard-pinning
dependencies versions. Please see its documentation for usage instructions.
In short, ``requirements.txt`` contains the list of direct requirements with
occasional version constraints (like ``Django<2``) and ``constraints.txt`` is
automatically generated from it by adding recursive tree of dependencies with fixed
versions.

To upgrade dependency versions, run ``scripts/pip-compile-sync.sh``.

If you just want to install the project as-is, simply install the generated ``.txt``
files, eg. ``pip install . -r requirements.txt -c constraints.txt``


Data Version Control
====================

.. code-block:: bash

  dvc pull
  dvc repro


Tests
=====
.. code-block:: bash

  pytest tests
