SHELL = /bin/bash


install:
	poetry install --no-root

g install-global:
	poetry install

update:
	poetry update


fmt:
	poetry run ruff format
	poetry run ruff check --select I --fix .

help:
	python -m llmcommitmsg -h

# Test commands to show output without committing.

diff:
	(git diff --cached --exit-code && git -P diff || git -P diff --cached)

run:
	$(MAKE) diff \
		| python -m llmcommitmsg

run-poll:
	export OPENAI_API_HOST='https://text.pollinations.ai/openai' \
		&& git diff --cached | python -m llmcommitmsg

# Run against fixed input.
sample:
	python -m llmcommitmsg < sample.diff
