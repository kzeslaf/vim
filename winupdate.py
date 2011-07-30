#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Kopiowanie plików do katalogu vim'a dla systemu windows.
"""

import sys
import os

if len(sys.argv) < 2:
	print('Too little parameters')
	sys.exit(1)

vimrc_src = os.path.join(sys.path[0], 'vimrc')
vimfiles_src = os.path.join(sys.path[0], 'vimfiles')

vimrc_dst = os.path.join(sys.argv[1], '_vimrc')
vimfiles_dst = sys.argv[1]

os.system('cp "' + vimrc_src + '" "' + vimrc_dst + '"')
os.system('cp -r "' + vimfiles_src + '" "' + vimfiles_dst + '"')
