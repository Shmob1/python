#!/usr/bin/env bash

set -x
scripts/pip-compile.sh && \
pip-sync constraints.txt && \
pip install -e .
