# LLM Commit Msg
> CLI tool to generate a commit message based on your Git diff - using an LLM

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/llm-commit-msg?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/llm-commit-msg/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")

## About

This tool works with an LLM model to interpret the Git diff, generate a commit message, then commit it.

Here are options for the LLM model:

- **Local LLM server** - Run at no cost and keeping your data private and offline.
- **OpenAI** - If you have a paid subscription for ChatGPT, configure with your credentials.
- **ChatGPT alternatives** - Use a free tool like [pollinations.ai](https://pollinations.ai) which uses the OpenAI API protocol.

## VS Code extension ideas

If you want this LLM logic as an _extension_ in VS Code instead of as a CLI, you can search the extensions marketplace for extensions that generate commit messages. There are many, though they tend to require a ChatGPT token and paid subscription and won't necessarily work with a local LLM or ChatGPT alternatives.


## Documentation

<div align="center">

[![View - Documentation](https://img.shields.io/badge/View-Documentation-blue?style=for-the-badge)](/docs/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
