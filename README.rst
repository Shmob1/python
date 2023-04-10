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

Tests
=====
.. code-block:: bash

  pytest tests
