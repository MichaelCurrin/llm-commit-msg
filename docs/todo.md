# TODO

- rewrite. This could be rewritten in Go so it can be packaged with dependencies as a binary.
    Or in JS where it can work as a VS Code extension. It could also run Git CLI.
- if no git diff, add staged? if you commit, it will be what is staged and will excl untracked files. If nothing is stage you'll get an error though, so could have fallback to make message and commit using unstaged if nothing found staged. Or give an error and the user must provide a flag to switch. And should commit reference directory like `.` or cached or pass through usual flags to git?
- Error handling for empty diff so it doesn't hallunicate
- add support for ollama - perhaps using langchain or keep openai and ollama libraries both used.
- Handle git diff errors better - exit can work if outside git repo except that the tab closes.
- Set max tokens - at least for output not input limit if possible.


---

Set flags or env variables for model/API
Set flag to force only
Setup with Poetry
Rename to shorter tool at least when installed
Real models
Set install instructions
Set log level and verbosity flag

---

Mypy
hooks
