#!/usr/bin/env python3
"""
Commit Message CLI tool.
"""
import sys
import os
import logging
import argparse

from openai import OpenAI

logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv("OPENAI_API_KEY", "dummy")
API_HOST = os.getenv("OPENAI_API_HOST", "http://localhost:1234/v1")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "local-model")

SYSTEM_PROMPT = """\
You are a helpful assistant that generates concise and informative Git commit messages based on the
provided diff, describing changes to all the files in the diff and summarising the changes at a high-level if necessary.

Provide a SINGLE commit message of ONE LINE, of length 50 to 72 characters, with optional description below,
and return NOTHING else.

Here is the conventional commit specification:

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


def get_openai_client(api_key: str, api_host: str) -> OpenAI:
    """
    Create and return an OpenAI client instance.
    """
    return OpenAI(api_key=api_key, base_url=api_host)


def request(
    client: OpenAI, model_name: str, system_prompt: str, user_prompt: str
) -> str:
    """
    Send a request to the OpenAI API and return the response.
    """
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
    except Exception:
        logging.exception("Error in API request")
        raise

    assert response.choices[0], "No results returned"
    message = response.choices[0].message

    if not message.content:
        raise ValueError("No content returned")

    return message.content.strip()


def request_llm(client: OpenAI, model_name: str, diff_content: str) -> str:
    """
    Generate a commit message based on the provided diff content.
    """
    user_prompt = f"{USER_PROMPT}\n\n{diff_content}"

    return request(client, model_name, SYSTEM_PROMPT, user_prompt)


def generate_commit_msg(diff_content: str) -> str:
    client = get_openai_client(API_KEY, API_HOST)

    return request_llm(client, MODEL_NAME, diff_content)


def main(args) -> None:
    """
    Main command-line entry-point.
    """
    parser = argparse.ArgumentParser(
        description="Generate a conventional commit message from a Git diff."
    )
    parser.add_argument(
        "diff",
        metavar="DIFF",
        nargs="?",
        help="The Git diff content to generate a commit message from. If not"
        " passed as an argument, this will be read from stdin.",
    )
    args = parser.parse_args()

    diff_content = args.diff if args.diff else sys.stdin.read()

    try:
        commit_msg = generate_commit_msg(diff_content)
    except Exception:
        logging.exception("Failed to generate commit message")
        sys.exit(1)

    print(commit_msg)


if __name__ == "__main__":
    main(sys.argv[1:])
