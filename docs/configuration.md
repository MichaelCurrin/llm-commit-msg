# Configuration

## Setup the alias

```ini
[alias]
	c = "!f() { \
		MSG=$(git diff --cached --exit-code && git -P diff || git -P diff --cached | ~/repos/llm-commit-msg/.venv/bin/python -m commitmsg); \
		git commit --edit -m \"$MSG\" && git log -n1; \
	}; f"
```

Set your environment variables in the function above `MSG` as `or in a shell config.

When run, this will:

1. Generate a commit message.
1. Pass the message to the Git `commit` command, but with a step for you to review and edit the message before finalizing the commit.

## Choose the AI server

Set as your environment variables in your shell config or shell session:

- `OPENAI_API_KEY`
- `OPENAI_API_HOST`
- `OPENAI_MODEL_NAME`
