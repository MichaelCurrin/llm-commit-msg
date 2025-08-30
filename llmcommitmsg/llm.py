#!/usr/bin/env python3
"""
LLM module.
"""

import argparse
import logging
import sys

from openai import OpenAI

from .constants import API_HOST, API_KEY, MODEL_NAME, SYSTEM_PROMPT, USER_PROMPT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        logger.exception("Error in API request")
        raise

    assert response.choices[0], "No results returned"
    message = response.choices[0].message

    if not message.content:
        raise ValueError("No content returned")

    return message.content.strip()


def request_llm(client: OpenAI, model_name: str, diff_content: str) -> str:
    """
    Generate a commit message using an LLM model and diff content.
    """
    logger.info("Requesting LLM")
    user_prompt = f"{USER_PROMPT}\n\n{diff_content}"

    return request(client, model_name, SYSTEM_PROMPT, user_prompt)


def generate_commit_msg(diff_content: str) -> str:
    """
    Return a generated commit message.
    """
    client = get_openai_client(API_KEY, API_HOST)

    return request_llm(client, MODEL_NAME, diff_content)


def main(args) -> None:
    """
    Main command-line entry-point.

    Expect diff diff on args or stdin and print the generated commit message.
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

    logger.debug("Diff portion: \n %s", diff_content[:200])

    try:
        commit_msg = generate_commit_msg(diff_content)
    except Exception:
        logger.exception("Failed to generate commit message")
        sys.exit(1)

    print(commit_msg)


if __name__ == "__main__":
    main(sys.argv[1:])
