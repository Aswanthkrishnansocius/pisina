from __future__ import annotations

import argparse
import re
import os.path
from typing import Sequence

def check_migration_folder(dir_list,condition_failed):
    for directory in dir_list:
        print(directory)
    return condition_failed




def main(argv: Sequence[str] | None = None) -> int:
    condition_failed = True
    # condition_failed = check_migration_folder(condition_failed)
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    dir_list = []
    for filename in args.filenames:
        dir = os.path.abspath(filename)
        dir_list.append(dir)
    print(dir_list)
    dir_list  = set(dir_list)
    condition_failed = check_migration_folder(dir_list,condition_failed)


        # if '' in dir:
        #     base = os.path.basename(filename)
        #     if (
        #             re.match("^test.*py$", base) or
        #             base == 'common.py'
        #     ):
        #         with open(filename, 'rb') as f:
        #             missing_tag = check_decorator(
        #                 f, missing_tag, filename=filename
        #             )
    return condition_failed
