# Usage

First start the LLM server.

## Help

```sh
$ make help
```

```
usage: lcm [-h] [--diff] [-d]

Generate a commit message using LLM and Git diff.

options:
  -h, --help     show this help message and exit
  --diff         Show the Git diff only and exit.
  -d, --dry-run  Generate the commit message using the LLM and print it and exit. This is a dry-run without commiting.
```

## Run app

Generate a commit message in the CLI and commit it.

```sh
$ lcm
```
