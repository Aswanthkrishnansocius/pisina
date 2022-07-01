from __future__ import annotations

import os.path
import git
from git import Repo
from git import Git


def check_up_to_date(mis_match):
    
    directory = os.getcwd()
    repo = Repo(directory)
    for data in repo.remote().fetch("--dry-run"):
        if data.flags != 4 and (data.remote_ref_path).strip() == "13.0":
            mis_match = True
            print(
                    f'[FD813].'
                    f'Your local repository is not up'
                    f'to date with production repository'
                )
    for data in repo.remote().pull("--dry_run"):
        print(data)
        print(data.flags)
    if repo.git.rev_list("..13.0"):
        mis_match = True
        print(
                    f'[FD813].'
                    f'Your branch is not up to date with origin/13.0'
                )
    return mis_match


def main():
    mis_match = False
    mis_match = check_up_to_date(mis_match)
    return True
