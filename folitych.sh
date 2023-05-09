#!/bin/bash

black --diff --check oversized setup.py
pylint --fail-under=10 oversized setup.py
mypy oversized setup.py
