# Usage

## Help

```sh
$ source .venv/bin/activate
```

```sh
$ python -m commitmsg -h
```

## Sample

Run against the hardcoded diff at [sample.diff](/sample.diff). This makes it easy to test prompt changes since the input is always the same.

```sh
$ make sample
```

## Run app

First navigate to the repo you are working on.

### Display

Generate a commit message in the CLI and simply display it.

```sh
$ git diff | (cd ~/repos/commit-msg && .venv/bin/python -m commitmsg)
```

Make it `git diff --cached` if you only want to use staged changes. This requires at least one file to be staged otherwise output will be blank.

### Commit

Run using the configured alias:

```sh
$ git c
```
