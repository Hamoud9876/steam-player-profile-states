# MakeFile

PYTHON_INTERPRETER = python
PIP = $(PYTHON_INTERPRETER) -m pip
WD = $(shell pwd)
PYTHONPATH = ${WD}
SHELL := /bin/bash

define activate_venv
	source venv/bin/activate && $1
endef

create-virtual-environment:
	@echo ">>> Setting up the virtualEnv. <<<"
	$(PYTHON_INTERPRETER) -m venv venv
	@echo ">>> Setting up the virtualEnv was completed"

install-requirements: create-virtual-environment
	@echo ">>> Installing requirements <<<"
	$(call activate_venv, $(PIP) install pip-tools)
	$(call activate_venv, pip-compile requirements.in)
	$(call activate_venv, $(PIP) install -r ./requirements.txt)
	@echo ">>> Finished installing requirements <<<"

## Install bandit
bandit:
	$(call activate_venv, $(PIP) install bandit)

## Install black
black:
	$(call activate_venv, $(PIP) install black)

## Install coverage
coverage:
	$(call activate_venv, $(PIP) install pytest-cov)

## Set up dev requirements (bandit, black & coverage)
dev-setup: bandit black coverage

## Run the security test (bandit + safety)
security-test:
	$(call activate_venv, bandit -lll */*.py *c/*/*.py)

## Run the black code check
run-black:
	$(call activate_venv, black ./src/*.py ./test/*.py ./db/*.py ./utility/*.py)

## Run the unit tests
unit-test:
	$(call activate_venv, PYTHONPATH=${PYTHONPATH} pytest -vv)

## Run the coverage check
check-coverage:
	$(call activate_venv, PYTHONPATH=${PYTHONPATH} pytest --cov=src test/)

run-all: security-test run-black unit-test check-coverage
