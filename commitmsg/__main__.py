#!/usr/bin/env python3
import sys
from openai import OpenAI

# Required to be not blank for local LLM to work.
API_KEY = "dummy"
API_HOST = "http://localhost:1234/v1"
# For now doesn't matter if only one model running and if not requesting an
# external API.
MODEL_NAME = "local-model"

SYSTEM_PROMPT = """\
    You are a helpful assistant that generates concise and informative Git
    commit messages based on the provided diff, describing changes to all the
    files in the diff and summarising the changes at a high-level if necessary.

    Provide a SINGLE commit message of ONE LINE, of length 50 to 72 characters, with optional description below,
    and return NOTHING else.

    Here is the conventional commit specficiation:

    - `feat` - feature
    - `fix`
    - `style`
    - `refactor`
    - `build` - a change in the build system.
    - `perf` - performance
    - `ci` - changes to the CI.
    - `docs` - changes to documentation files or docs in code.
    - `test` - relating to running tests.
    - `chore` - changes to configs, file renames or moves, changes to dependencies.
    - `revert`

    Create commits based on that.
    e.g. feat: Add foo to bar.
"""

USER_PROMPT = "Generate a single one-line conventional commit message and nothing else, using the following Git diff:"


def request(client, model_name: str, system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    result = response.choices[0]

    return result.message.content.strip()


def get_commit_message(diff_content: str) -> str:
    client = OpenAI(api_key=API_KEY, base_url=API_HOST)
    user_prompt = f"{USER_PROMPT}\n\n{diff_content}"

    try:
        return request(client, MODEL_NAME, SYSTEM_PROMPT, user_prompt)
    except Exception as e:
        return f"Error generating commit message: {str(e)}"


def main() -> None:
    """
    Main command-line entry-point.
    """
    diff_content = sys.stdin.read()

    commit_message = get_commit_message(diff_content)
    print(commit_message)


if __name__ == "__main__":
    main()
