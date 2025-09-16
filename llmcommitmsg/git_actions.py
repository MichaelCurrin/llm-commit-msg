"""
Git actions module.
"""

import logging
import sys

from git import GitCommandError, Repo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _has_working_tree_changes(repo: Repo) -> bool:
    """
    Return True if there are unstaged changes in the repo.
    """
    return repo.is_dirty(index=False, working_tree=True)


def get_repo() -> Repo:
    """
    Return configured Repo instance using the current directory or parent
    directories.
    """
    return Repo(search_parent_directories=True)


def _has_staged_changes(repo: Repo) -> bool:
    """
    Return True if there are changed staged in the repo.
    """
    return repo.is_dirty(index=True, working_tree=False)


def get_diff(repo: Repo) -> str:
    """
    Get the diff for the repository. Prioritize staged changes, fall back to
    working tree.
    """
    try:
        if _has_staged_changes(repo):
            logging.info("Using staged changes for the diff.")
            return repo.git.diff("--cached")

        if _has_working_tree_changes(repo):
            logging.info(
                "No staged changes found. Using working tree changes for the diff."
            )
            return repo.git.diff()
    except GitCommandError as e:
        logging.error("Error accessing Git repository: %s", e)
        sys.exit(1)

    logging.error("No changes to commit.")
    sys.exit(1)


def commit_with_message(repo: Repo, message: str) -> None:
    """
    Commit changes with the provided message. Prioritize staged changes, fall
    back to working tree.
    """
    try:
        if _has_staged_changes(repo):
            repo.index.commit(message)
            logging.info("Commit successful (staged changes)!")
            return

        if _has_working_tree_changes(repo):
            # Add all changes to the index.
            repo.git.add(A=True)
            repo.index.commit(message)
            logging.info("Commit successful (working tree changes)!")
            return
    except GitCommandError as e:
        logging.error("Error committing changes: %s", e)
        sys.exit(1)

    logging.error("No changes to commit.")
    sys.exit(1)
