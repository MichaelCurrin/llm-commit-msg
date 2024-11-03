# Usage

First start the LLM server.

## Help

```sh
$ python -m commitmsg -h
```

## Run app

Generate a commit message in the CLI and simply display it.

```sh
$ git diff || exit 1; (cd ~/repos/commit-msg && venv/bin/python -m commitmsg)
```

## Commit

Run using the configured alias:

```sh
$ git c
```
