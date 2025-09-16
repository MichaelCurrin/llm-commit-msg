# Configuration

The default settings as assume you have Ollama running locally and want to use `gemmma3`. Or use the settings below.

## Variables

Set these as global variables in your shell:

- `OPENAI_API_KEY`
- `OPENAI_API_HOST`
- `OPENAI_MODEL_NAME`

## Configuration flows

### Change Ollama model

e.g. for Ollama just set the model name:

```sh
export OPENAI_MODEL_NAME='code-llama'
```

### Use OpenAI API

```sh
export OPENAI_API_KEY="******"
export OPENAI_API_HOST='https://api.openai.com/v1'
export OPENAI_MODEL_NAME='model-name'
```

### Use Pollinations API

e.g. For Pollinations AI using model from [models](https://text.pollinations.ai/models).

```sh
export OPENAI_API_HOST='https://text.pollinations.ai/openai'
export OPENAI_MODEL_NAME='openai'
```
