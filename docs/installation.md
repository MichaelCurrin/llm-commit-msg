# Installation

## Install Python project

Install Python 3 with version as set in [pyproject.toml](/pyproject.toml).

Install with pip:

```sh
$ pip install git+https://github.com/MichaelCurrin/llm-commit-msg
```

Or with [pipx](https://pipx.pypa.io/stable/) for managing in an isolate environment.

```sh
$ pip install pipx
$ pipx install git+https://github.com/MichaelCurrin/llm-commit-msg
```

## Setup a LLM server locally

If you want you to use a local LLM solution for free and private use, follow these steps. Ollama is recommended.

### Ollama

1. Install Ollama. See [Ollama homepage](https://ollama.com/).
1. Start Ollama.

### LM Studio

1. Install LM Studio.
1. Open LM Studio.
1. Install a model.
1. Run model with local server.
