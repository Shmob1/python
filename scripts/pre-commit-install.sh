#!/usr/bin/env bash

set -x
pre-commit install \
--install-hooks \
--hook-type pre-commit \
--hook-type commit-msg \
--hook-type pre-push \
--hook-type post-checkout
