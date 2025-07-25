ENV = /bin/bash


install:
	pip install pip --upgrade
	pip install -r requirements.txt


help:
	python -m commitmsg -h

diff:
	(git diff --cached --exit-code && git -P diff || git -P diff --cached)

run:
	$(MAKE) diff \
		| python -m commitmsg

run-poll:
	export OPENAI_API_HOST='https://text.pollinations.ai/openai' \
		&& git diff --cached | python -m commitmsg

sample:
	python -m commitmsg < sample.diff
