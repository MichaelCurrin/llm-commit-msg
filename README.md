# LLM Commit Msg
> CLI tool to generate a commit message with an LLM then commit it

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/llm-commit-msg?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/llm-commit-msg/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMichaelCurrin%2Fllm-commit-msg%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=$.tool.poetry.dependencies.python&label=python&logo=python&logoColor=white)](https://python.org "Go to Python homepage")

## About

This tool works with an LLM model to read the Git diff from changed files, generate a commit message, then commit with it.

Here are options for choosing an LLM model:

- **Local LLM server** - Run at no cost and keeps your data **private** and **offline**. This requires you to have an LLM server installed, but with Ollama this can be done in one effortless step.
- **OpenAI** - If you have a paid subscription for ChatGPT, you can configure with your credentials. Then you can use a better model and don't need a local server running.
- **ChatGPT alternatives** - Use a service like [pollinations.ai](https://pollinations.ai) which uses the OpenAI API protocol. This is free and might be higher quality than a local model, but your code is no longer private and you can hit rate limiting issues.

## Motivation for using this tool

- Generate commit messages in the CLI without being tied to an IDE, or if your IDE doesn't have a button to generate commit messages.
- Keep your private code private - use a local LLM without internet access and no cost.
- Full control over the prompt for writing commit messages (though you have to clone this repo to customize that).

## Quickstart

```sh
$ pip install git+https://github.com/MichaelCurrin/llm-commit-msg
```

Run:

```sh
$ lcm --help
```

Or run without flags to generate a commit message and commit it. The default settings as assume you have Ollama running locally.

## Documentation

<div align="center">

[![View - Documentation](https://img.shields.io/badge/View-Documentation-blue?style=for-the-badge)](/docs/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
