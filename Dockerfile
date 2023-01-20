FROM python:3.10-slim

SHELL ["/bin/bash", "-c"]

# first copy a minimal set of files required to install the dependencies
COPY environment.yaml environment.yaml
COPY requirements* .
COPY constraints.txt constraints.txt
COPY scripts scripts
COPY setup.py setup.py

# create some empty dummy files required for installation
RUN mkdir my_project && \
    touch my_project/__init__.py && \
    touch README.rst

# install the python requirements
RUN pip install pip-tools && \
    pip-sync constraints.txt && \
    pip freeze

# now the expensive part is done, copy everything else in
COPY . .

RUN pip install -e .
