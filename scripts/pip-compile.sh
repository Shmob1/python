#!/usr/bin/env bash

set -x
CUSTOM_COMPILE_COMMAND="scripts/pip-compile.sh" \
pip-compile --strip-extras requirements.txt -o constraints.txt && \
pip-compile --strip-extras requirements-dev.txt -o constraints-dev.txt --no-header && \
cat constraints-dev.txt >> constraints.txt && \
rm constraints-dev.txt
