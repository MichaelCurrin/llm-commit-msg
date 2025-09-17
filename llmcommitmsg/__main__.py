#!/usr/bin/env python3
"""
LLM commit message application.

Main entry point for generating commit messages and committing changes.
"""

import argparse
import logging

from . import git_actions, llm

logger = logging.getLogger(__name__)

# Match with poetry scripts.
APP_CMD = "lcm"


def run(show_diff=False, show_message=False, diff=None) -> None:
    """
    Main logic to generate a diff and a commit message and commit it.

    :param show_diff: If True, show the Git diff only and exit.
    :param show_message: If True, generate the commit message and print it then
        exit.
    """
    if not diff:
        repo = git_actions.get_repo()
        diff = git_actions.get_diff(repo)

    if show_diff:
        print(diff)
        return

    commit_msg = llm.generate_commit_msg(diff)

    if show_message:
        print(commit_msg)
        return

    git_actions.commit_with_message(repo, commit_msg)


def main() -> None:
    """
    Main command-line entry-point.
    """
    parser = argparse.ArgumentParser(
        description="Generate a commit message using LLM and Git diff.",
        prog=APP_CMD,
    )

    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Generate the commit message using the LLM and print it and exit."
        " This is a dry-run without commiting.",
    )
    parser.add_argument(
        "--diff",
        help="Optionally provide the Git diff to the app directly as text, for development or debugging purposes."
        " If not provided, the app will read from Git repo.",
    )
    parser.add_argument(
        "-l",
        "--log-level",
        default="ERROR",
        choices=["INFO", "ERROR"],
        help="Logging level (default: ERROR).",
    )
    parser.add_argument(
        "--show-diff",
        action="store_true",
        help="Show the Git diff only and exit. This is useful for debugging the Git integration.",
    )

    args = parser.parse_args()

    log_level_number = logging.getLevelNamesMapping()[args.log_level]
    logging.basicConfig(
        level=log_level_number,
        format="%(levelname)s:%(name)s:%(message)s",
    )
    run(show_diff=args.show_diff, show_message=args.dry_run, diff=args.diff)


if __name__ == "__main__":
    main()
