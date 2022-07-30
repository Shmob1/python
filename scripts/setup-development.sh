#!/usr/bin/env bash

set -x
pip install pip-tools
scripts/pip-compile-sync.sh && \
scripts/pre-commit-install.sh
