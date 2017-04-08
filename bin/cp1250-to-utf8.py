#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
==========================
Program: cp1250-to-utf8.py

Usage:
    ./cp1250-to-utf8.py [--extensions h,hpp,cpp] directory1 [directory2, ...]

Program options:
    -e/--extensions - list of comma separated file extensions to convert

Description:
    Program is usefull for converting polish language source files from
    cp1250 encoding to utf8 encoding.

    Program browse recursively selected directories and converts encoding
    of files with selected extensions (default: h,hpp,cpp).

    Program omits directories '.svn' and '.git'.
"""


import sys
import os
import tempfile
import optparse


##############################
# config
##############################

PROCESSED_EXTENSIONS = ['h', 'hpp', 'cpp']
OMITTED_DIRS = ['.svn', '.git']

POLISH_CHARS_CP1250 = [0xA5, 0xC6, 0xCA, 0xA3,
                       0xD1, 0xD3, 0x8C, 0x8F,
                       0xAF, 0xB9, 0xE6, 0xEA,
                       0xB3, 0xF1, 0xF3, 0x9C,
                       0x9F, 0xBF]

##############################
# ret values
##############################

RET_ERROR = 1
RET_INVALID_PARAMS = 2

##############################
# functions
##############################

def is_cp1250(f):
    """Return True when file is cp1250 encoded and False otherwise."""
    result = False
    with open(f, 'rb') as fp:
        b = fp.read()
        for i in b:
            i = ord(i)
            if i >= 128 and i not in POLISH_CHARS_CP1250:
                return False
            if i >= 128:
                result = True
    return result


def convert_encoding(directory, f):
    """Convert file encoding from cp1250 to utf-8."""
    with open(f, 'rb') as fp:
        b = fp.read()

    tempname = ""
    prefix = os.path.split(f)[1] + '.'

    with tempfile.NamedTemporaryFile(prefix=prefix, dir=directory, delete=False) as fp:
        tempname = fp.name
        fp.write(b.decode('cp1250').encode('utf-8'))

    if sys.platform == 'win32':
        os.remove(f)

    os.rename(tempname, f)


def process_directory(d, processed_extensions):
    """Browse directory recursively and convert encoding of selected files.

       Function omits directories defined in OMITTED_DIRS list.
    """
    files = os.listdir(d)
    for f in files:
        p = os.path.join(d, f)
        if os.path.isdir(p):
            if f in OMITTED_DIRS:
                continue
            process_directory(p, processed_extensions)
        else:
            if os.path.splitext(p)[1][1:] in processed_extensions and is_cp1250(p):
                print 'Converting file: ' + p
                convert_encoding(d, p)


def main():
    """Program entry."""

    # parse cmd line
    parser = optparse.OptionParser(optparse.SUPPRESS_USAGE, add_help_option=False)
    parser.add_option("-h", "--help", dest="help", action='store_true')
    parser.add_option("-e", "--extensions", dest="extensions",
                      default=','.join(PROCESSED_EXTENSIONS))
    (options, args) = parser.parse_args()

    # print help message (also when no directories where supplied)
    if options.help or len(args) < 1:
        print __doc__
        sys.exit(RET_INVALID_PARAMS)

    # setup extensions
    processed_extensions = options.extensions.split(',')
    print 'Processed extensions: ' + str(processed_extensions)

    # process directories
    for d in args:
        print 'Processing directory: ' + d
        process_directory(d, processed_extensions)


##############################
# main
##############################

if __name__ == '__main__':

    try:
        main()
    except Exception as e:
        print e
        print 'Quit...'
        sys.exit(RET_ERROR)

    print 'DONE'
