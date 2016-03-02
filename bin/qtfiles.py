#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
USAGE:
    ./qtfiles path/to/*.files
"""


import os
import re
import sys


#######################
# Constants
#######################


FILES_TYPES = [
    'Doxyfile',
    'Makefile',
    'SConscript',
    'SConstruct',
    'VERSION',
    r'.*\.dox',
    r'.*\.h',
    r'.*\.cpp',
    r'.*\.txt\.template',
]


OMITTED_DIRS = r'.*(buildtools|third-party).*'


######################
# Functions
######################


def get_files(path, qtproj_path):
    """..."""
    result = []

    for dirpath, dirnames, filenames in os.walk(path):

        if re.match(OMITTED_DIRS, dirpath):
            continue

        for f in filenames:
            for r in FILES_TYPES:
                if re.match(r, f):
                    result.append(os.path.join(os.path.relpath(dirpath, os.path.join(path, qtproj_path)), f))
                    break

    return sorted(result, key=lambda f: (os.path.dirname(f), os.path.basename(f)))


def main():
    """..."""
    try:
        files_path = os.path.abspath(sys.argv[1])
    except (IndexError, ValueError):
        print(__doc__)
        return

    cwd = os.path.abspath(os.getcwd())
    files = get_files(cwd, os.path.split(files_path)[0])

    with open(files_path, 'w') as f:
        for i in files:
            f.write(i + '\n')


######################
# Main
######################


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(1)
