#!/usr/bin/env python3
"""
LLM commit message application.

Main entry point for generating commit messages and committing changes.
"""

import argparse
import logging

from . import git_actions, llm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run(show_diff=False, show_message=False) -> None:
    """
    Main entry-point for the application.

    Run the application using the provided flags.

    :param show_diff: If True, show the Git diff only and exit.
    :param show_message: If True, generate the commit message and print it, but do not commit.

    :returns: None
    """
    repo = git_actions.get_repo()

    diff = git_actions.get_diff(repo)

    if show_diff:
        print(diff)
        return

    commit_msg = llm.generate_commit_msg(diff)

    if show_message:
        print("Generated Commit Message:\n")
        print(commit_msg)
        return

    commit_msg = llm.generate_commit_msg(diff)
    # git_actions.commit_with_message(repo, commit_msg)


def main():
    """
    Main command-line entry-point.
    """
    parser = argparse.ArgumentParser(
        description="Generate a commit message using LLM and Git diff."
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Show the Git diff only and exit.",
    )
    parser.add_argument(
        "--msg",
        action="store_true",
        help="Generate the commit message using the LLM and print it and exit."
        "If the `--diff` flag is added with this, that will be ignored",
    )

    args = parser.parse_args()

    run(show_diff=args.diff, show_message=args.msg)


if __name__ == "__main__":
    main()
