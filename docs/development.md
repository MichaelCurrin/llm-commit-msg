# Development

Install Python 3 with version as set in [pyproject.toml](/pyproject.toml).

Clone the repo.

## Setup project

Install project packages in an isolated enviroment with Poetry:

```sh
$ make install
```


## Display help

```sh
$ make help
```


## Run app directly

```sh
poetry run python -m llmcommitmsg
```

## Install global from local repo

Install `pipx` - see the [docs](https://pipx.pypa.io/stable/).

Install app globally:

```sh
$ make g
```

Uninstall:

```sh
$ pipx uninstall llmcommitmsg
```
