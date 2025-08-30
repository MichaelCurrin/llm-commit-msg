ENV = /bin/bash


install:
	pip install pip --upgrade
	pip install -r requirements.txt

fmt:
	ruff format
	ruff check --select I --fix .

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
