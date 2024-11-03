# Commit Msg
> CLI tool to generate a commit message based on your Git diff - using a local LLM

## About

This tool works an LLM model to interpret the Git diff and generate a commit message. There are two options then:

- This can be run using a local LLM server, at a no cost.
- If you have a paid subscription for ChatGPT, you can use configure against your credentials instead.

## Alternatives

If you want this logic as an extension is VS Code instead of CLI, you can search the extensions marketplace for extensions that generate commit messages as there are a lot, though they tend to require a ChatGPT token and paid subscription.

## TODO

- rewrite. This could be rewritten in Go so it can be packaged with dependencies as a binary
    Or in JS where it can work as a VS Code extension. It could also run Git CLI
- if no diff, add staged?
- Error handling for empty diff so it doesn't hallunicate
