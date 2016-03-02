#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
USAGE:
    ./pycheck path_to_file_or_dir
"""


import os
import sys


#########################
# Constants
#########################


PEP8 = 'pep8 --ignore=E501,E701 '
PYFLAKES = 'pyflakes '


#########################
# Functions
#########################


def check_file(path):
    """..."""
    return os.system(PEP8 + path) or os.system(PYFLAKES + path)


def main():
    """..."""
    try:
        path = sys.argv[1]
    except (IndexError, ValueError):
        print(__doc__)
        return 0

    if os.path.isfile(path):
        return check_file(path)

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if f.endswith('.py'):
                if check_file(os.path.join(dirpath, f)) != 0:
                    return 1


#########################
# Main
#########################


if __name__ == '__main__':
    try:
        res = main()
    except Exception as e:
        print(e)
        sys.exit(1)

    sys.exit(res)
