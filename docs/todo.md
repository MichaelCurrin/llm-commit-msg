# TODO

## Ideas

- rewrite.
    - I have this in Go, just have to keep changes repeated or pick one to focus on.
    - Or in JS where it can work as a VS Code extension. It could also run Git CLI.
- Set max tokens - at least for output not input limit if possible.
- Allow prompt override.
- See if simpler prompt works now with better model - see Go repo.

## Diff

- if no git diff, add staged?
    if you commit, it will be what is staged and will excl untracked files. If nothing is stage you'll get an error though,  so could have fallback to make message and commit using unstaged if nothing found staged.

    Or give an error and the user must provide a flag to switch. And should commit reference directory like `.` or cached or pass through usual flags to git?
- Error handling for empty diff so it doesn't hallunicate
- Handle git diff errors better - exit can work if outside git repo except that the tab closes.


## Configuration and setup

Set flags or env variables for model/API

Mypy


## Commit message flow

add step to **edit** message before committing - can be in Python app and then pass to git

maybe option to **retry** or **cancel**

otherwise at least **print** the commit message


## Logging and verbosity

Set log level and verbosity flag:

make info as debug
or set log level as error, unless running local install - does pipx allow passing a flag?
