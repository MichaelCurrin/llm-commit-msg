SHELL = /bin/bash

DEV_LOG_LEVEL = INFO

all: install check test

h help:
	@grep '^[a-z]' Makefile

install:
	poetry install --no-root

update:
	poetry update

g install-global:
	pipx install .



check:
	poetry build
	poetry run ruff format --check
	poetry run ruff check --select I .

fmt:
	poetry run ruff format
	poetry run ruff check --select I --fix .

test:
	PYTHONPATH=. poetry run pytest


run-help:
	poetry run python -m llmcommitmsg -h

# Local debugging commands with dry-run.

# Use changes in the repo itself.

run-repo:
	poetry run python -m llmcommitmsg --dry-run --log-level $(DEV_LOG_LEVEL)

# Use hardcoded input.

sample:
	poetry run python -m llmcommitmsg \
		--dry-run \
		--log-level $(DEV_LOG_LEVEL) \
		--diff "$$(cat sample.diff)"

sample-poll:
	export OPENAI_API_HOST='https://text.pollinations.ai/openai' \
		| poetry run python -m llmcommitmsg \
			--dry-run \
			--log-level $(DEV_LOG_LEVEL) \
			--diff "$$(cat sample.diff)"
