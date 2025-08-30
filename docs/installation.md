# Installation

Note: Windows is not supported.

## Install

Python project:

1. Install Python 3.
1. Create a virtual environment.
    ```sh
    $ python -m venv .venv
    ```
1. Install packages.
    ```sh
    $ make install
    ```

LLM server:

1. Install LM Server.
1. Install a model.
1. Run model with local server.

## Configuration.

Setup the alias:

```ini
[alias]
	c = "!f() { \
		export OPENAI_API_HOST='https://text.pollinations.ai/openai'; \
		MSG=$(git diff --cached | (cd ~/repos/llm-commit-msg && .venv/bin/python -m llmcommitmsg)); \
		git commit --edit -m \"$MSG\" && git log -n1; \
	}; f"
```

Remove `--cached` if you want to look at all modified files and not just staged changes.

When run, this will:

1. Generate a commit message.
1. Pass the message to the Git `commit` command, but with a step for you to review and edit the message before finalizing the commit.
