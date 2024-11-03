ENV = /bin/bash

install:
	pip install pip --upgrade
	pip install -r requirements.txt


help:
	python -m commitmsg -h

run:
	python -m commitmsg

sample:
	python -m commitmsg < sample.diff
