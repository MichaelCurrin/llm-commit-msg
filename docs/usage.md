# Usage

## Help

```sh
$ source .venv/bin/activate
```

```sh
$ python -m commitmsg -h
```

## Run app

First navigate to the repo you are working on.

### Display

Generate a commit message in the CLI and simply display it.

```sh
$ git diff | (cd ~/repos/commit-msg && .venv/bin/python -m commitmsg)
```

### Commit

Run using the configured alias:

```sh
$ git c
```
