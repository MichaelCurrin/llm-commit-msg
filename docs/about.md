# About

## Project overview

The LLM Commit Msg project is a command-line tool that generates conventional commit messages by analyzing Git diffs using Large Language Models (LLMs).

The tool supports both local LLM servers (like Ollama) and cloud-based services (like OpenAI), providing users with intelligent, context-aware commit message generation while maintaining privacy and cost-effectiveness through local model options.

## Values

- Ease of use
- Security (using local LLM or self-hosted cloud LLMs are recommended over using subscription ChatGPT API)
- Quality of input

Speed is limited by what your local machine can do and what model can do, there is no much possible to improve on here.

## Requirements

- **Core Functionality**: Generate conventional commit messages from Git diffs using LLM models
- **LLM Integration**: Support multiple LLM providers including local servers (Ollama) and cloud services (OpenAI)
- **Git Integration**: Read staged and unstaged changes, handle Git repository validation and error cases
- **Conventional Commits**: Generate properly formatted commit messages following conventional commit specification
- **Cross-Platform Support**: Work on Linux and macOS
- **CLI Interface**: Provide command-line interface with argument parsing and help documentation
- **Error Handling**: Graceful handling of empty diffs, API failures, and Git repository errors
- **Configuration**: Environment-based configuration for API keys, hosts, and model names
- **Documentation**: Comprehensive usage guides, installation instructions, and configuration documentation
- **Performance**: Handle large file changes efficiently with appropriate diff strategies
