#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
ksvn.py - decorator for svn tools allowing for simultaneous
operations on many working copies.

Additional commands when inside working copy:
    - clear: remove all unversioned files

Commands outside working copy:
    - info
    - update

TODO:
    - make the script work for python3
    - better output
    - 'clear' asks user for confirmation
    - dodać polecenie 'stat'
"""


import os
import subprocess
import sys
import traceback


#######################
# Functions
#######################


def is_working_copy(path):
    """..."""
    while path != '' and path != '/':
        if os.path.exists(os.path.join(path, '.svn')):
            return True
        path = os.path.abspath(os.path.join(path, '..'))
    return False


def list_working_copies(path):
    """..."""
    result = []

    for i in os.listdir(path):
        p = os.path.join(path, i)
        p = os.path.join(p, '.svn')

        if os.path.exists(p):
            result.append(i)

    return result


def svn_info(path_list):
    """..."""
    for i in path_list:
        output = subprocess.check_output(['svn', 'info', '{}'.format(i)])
        for line in output.split('\n'):
            if line.startswith('Relative URL'):
                print('[{}] {}'.format(i, line))
    return 0


def svn_update(path_list):
    """..."""
    for i in path_list:
        res = os.system('( echo Directory: [{0}]; cd {0}; svn update )'.format(i))
        if res != 0:
            return res
    return 0


def main():
    """..."""
    cwd = os.getcwd()

    #
    #
    #
    if is_working_copy(cwd):
        if sys.argv[1] == 'clear':
            return os.system(r"rm -rf `svn status --no-ignore | grep '^[\?I]' | sed 's/^[\?I]//'`")
        else:
            return os.system('svn ' + ' '.join(sys.argv[1:]))

    #
    #
    #
    wc_list = sorted(list_working_copies(cwd))

    if sys.argv[1] == 'info':
        return svn_info(wc_list)
    elif sys.argv[1] in ['up', 'update']:
        return svn_update(wc_list)
    else:
        raise Exception('Unknown command: {}'.format(sys.argv[1]))


#######################
# Main
#######################


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
        sys.exit(1)
