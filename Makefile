SHELL = /bin/bash

all: install check

install:
	poetry install --no-root

g install-global:
	pipx install .

update:
	poetry update


check:
	poetry build
	poetry run ruff format --check
	poetry run ruff check --select I .

fmt:
	poetry run ruff format
	poetry run ruff check --select I --fix .


help:
	poetry run python -m llmcommitmsg -h

# Test commands to show output without committing.

diff:
	(git diff --cached --exit-code && git -P diff || git -P diff --cached)

run:
	$(MAKE) diff \
		| poetry run python -m llmcommitmsg

run-poll:
	export OPENAI_API_HOST='https://text.pollinations.ai/openai' \
		&& $(MAKE) diff \
		| poetry run python -m llmcommitmsg

# Run against fixed input.
sample:
	poetry run python -m llmcommitmsg < sample.diff
