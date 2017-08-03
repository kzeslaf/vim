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
    'Jenkinsfile',
    'Makefile',
    'SConscript',
    'SConstruct',
    'VERSION',
    r'.*\.dox',
    r'.*\.h',
    r'.*\.cpp',
    r'.*\.xml',
    r'.*\.txt\.template',
    r'README\.*',
]


OMITTED_DIRS = [
    '.git',
    '.svn',
    'buildtools',
    'third-party',
]


######################
# Functions
######################


def get_files(path, qtproj_path):
    """..."""
    result = []

    files = map(lambda x: os.path.join(path, x),  os.listdir(path))

    for i in files:
        if os.path.isdir(i) is True:
            if os.path.split(i)[1] in OMITTED_DIRS:
                continue
            result += get_files(i, qtproj_path)

        for r in FILES_TYPES:
            if re.match(r, os.path.split(i)[1]):
                result.append(os.path.relpath(i, qtproj_path))
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
