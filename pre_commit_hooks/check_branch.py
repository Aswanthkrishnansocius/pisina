from __future__ import annotations

import argparse
import re
import os.path
from typing import Sequence
import git
from git import Repo


def check_up_to_date():
    repo = Repo(self.rorepo.working_tree_dir)
    print(repo)
    result = repo.remote().fetch()
    print(result)
    return True


def main():
    mis_match = True
    mis_match = check_up_to_date()

    return mis_match