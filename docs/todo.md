# TODO

- Find prompts others have written or change models - the output sometimes not relevant or specific enough and misses conventional commit prefix. Maybe break conventional commit into separate LLM call, at cost of speed.
- For large file changes, use git st or diff-index instead and see how that performs (different prompt though)
- Make installable Python package. Even if based on repo, at least install in bin for Windows and Unix.
- rewrite. This could be rewritten in *Go* so it can be packaged with dependencies as a binary.
    Or in JS where it can work as a VS Code extension. It could also run Git CLI.
- if no git diff, add staged? if you commit, it will be what is staged and will excl untracked files. If nothing is stage you'll get an error though, so could have fallback to make message and commit using unstaged if nothing found staged. Or give an error and the user must provide a flag to switch. And should commit reference directory like `.` or cached or pass through usual flags to git?
- Error handling for empty diff so it doesn't hallunicate
- add support for ollama - perhaps using langchain or keep openai and ollama libraries both used.
- Handle git diff errors better - exit can work if outside git repo except that the tab closes.
- Set max tokens - at least for output not input limit if possible.
