# Usage

First start the LLM server.

## Help

```sh
$ python -m llmcommitmsg -h
```

## Run app

Generate a commit message in the CLI and simply display it.

```sh
$ git diff | (cd ~/repos/commit-msg && venv/bin/python -m llmcommitmsg)
```

## Commit

Run using the configured alias:

```sh
$ git c
```
