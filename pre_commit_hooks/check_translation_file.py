from __future__ import annotations
import argparse
import polib
import os.path
from typing import Sequence
from collections import Counter






def searchDuplicates(po_file_path, duplicate):
    """
    Log all those msgid duplicated inside the file
    """
    duplicate = duplicate
    po_file = po_file_path
    msg_ids = [entry.msgid for entry in po_file]
    counter_dict = Counter(msg_ids)
    if any(el for el in counter_dict.values() if el > 1):
        print("========== Duplicates Terms are found! ==========")
        print('========== Manual Intervention is needed """"""""')
        duplicate = True

    for key, value in counter_dict.items():
        if value > 1:
            print(key)
            print(value)
    return duplicate


def sort_entries(po_file_path, duplicate, save=False):
    """
    Sort a po file
    :rtype: object
    """
    print("entered")
    po_sorted = polib.POFile()
    po_file = polib.pofile(po_file_path)
    for entry in sorted(po_file, key=lambda x: x.msgid):
        po_sorted.append(entry)
    print(type(po_sorted))
    print(type(po_file_path))
    print(po_sorted == po_file) 
    if po_sorted != po_file and save:
        file_name = po_file_path
        print("File Sorted", file_name)
        po_sorted.save(file_name)
        searchDuplicates(po_sorted)
        return True
    return searchDuplicates(po_sorted,duplicate)
    






def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    duplicate = False
    for filename in args.filenames:
        base = os.path.basename(filename)
        if (re.match(".po$", base)):
            duplicate = sortEntries(filename,duplicate,True,)
            
    print(duplicate)
    return True





if __name__ == "__main__":
    raise SystemExit(main())


# f = open("/home/socius/fr_CH.po", "r")
# file = f.read()
# sortEntries('/home/socius/fr_CH.po',False,True)
