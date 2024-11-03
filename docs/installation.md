# Installation

Note: Windows is not supported.

## Install

Python project:

1. Install Python 3.
1. Create a virtual environment.
    ```sh
    $ python -m venv venv
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
    c = '! git commit --edit -m "$(cd ~/repos/commit-msg && venv/bin/python -m commitmsg)"'
```

When run, this will:

1. Generate a commit message.
1. Pass the message to the Git `commit` command, but with a step for you to review and edit the message before finalizing the commit.
