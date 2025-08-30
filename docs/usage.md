# Usage

## Help

```console
$ lcm --help
usage: lcm [-h] [--diff] [-d]

Generate a commit message using LLM and Git diff.

options:
  -h, --help     show this help message and exit
  --diff         Show the Git diff only and exit.
  -d, --dry-run  Generate the commit message using the LLM and print it and exit. This is a dry-run without commiting.
```

## Run app

First start the LLM server.

Run this command to generate a commit message in the CLI and commit it.

```sh
$ lcm
```
