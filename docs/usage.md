# Usage

## Help

```sh
$ source .venv/bin/activate
```

```sh
$ python -m llmcommitmsg -h
```

## Sample

Run against the hardcoded diff at [sample.diff](/sample.diff). This makes it easy to test prompt changes since the input is always the same.

```sh
$ make sample
```

## Run app

First navigate to the repo you are working on.

Make changes you want to commit. Optionally stage changes you want to commit otherwise unstaged changes will be used.

### Display

Generate a commit message in the CLI and simply display it.

```sh
$ (git diff --cached --exit-code && git -P diff || git -P diff --cached) | ~/repos/llm-commit-msg/.venv/bin/python -m llmcommitmsg
```

### Commit

Run using the configured alias:

```sh
$ git c
```
