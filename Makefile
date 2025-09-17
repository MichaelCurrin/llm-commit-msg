SHELL = /bin/bash

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


diff:
	(git diff --cached --exit-code && git -P diff || git -P diff --cached)


run-help:
	poetry run python -m llmcommitmsg -h

run:
	$(MAKE) diff \
		| poetry run python -m llmcommitmsg

sample:
	poetry run python -m llmcommitmsg < sample.diff

sample-poll:
	export OPENAI_API_HOST='https://text.pollinations.ai/openai' \
		&& $(MAKE) diff \
		| poetry run python -m llmcommitmsg
