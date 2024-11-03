# TODO

- Make installable Python package. Even if based on repo, at least install in bin for Windows and Unix.
- rewrite. This could be rewritten in Go so it can be packaged with dependencies as a binary
    Or in JS where it can work as a VS Code extension. It could also run Git CLI
- if no diff, add staged?
- Error handling for empty diff so it doesn't hallunicate
- add support for ollama - perhaps using langchain or keep openai and ollama libraries both used.
- Handle git diff errors better - exit can work if outside git repo except that the tab closes.
