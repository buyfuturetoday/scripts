#!/usr/bin/env python3
# vim:fileencoding=utf-8:ft=python
# file: sha256.py
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2014-12-28 13:36:38 +0100
# Last modified: 2017-06-04 13:54:14 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to sha256.py. This work is published from the
# Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/
"""
Calculate the SHA256 checksum of files.

Meant for systems that don't come with such a utility.
"""

from hashlib import sha256
from os.path import isfile
from sys import argv, exit
import argparse

__version__ = '1.0.2'


def main(argv):
    """
    Entry point for sha256.

    Arguments:
        argv: command line arguments
    """
    parser = argparse.ArgumentParser(description=__doc__)
    hs = '''compare file to this sha256 string;
            will add "[ OK ]" or "[ Failed ]" after the checksum'''
    parser.add_argument('-c', '--checksum', default=None, help=hs)
    parser.add_argument(
        '-v', '--version', action='version', version=__version__)
    parser.add_argument('file', nargs='*')
    args = parser.parse_args(argv)
    if not args.file:
        parser.print_help()
        exit(0)
    if args.checksum and len(args.checksum) != 64:
        print('Invalid checksum length. Skipping comparison.')
        args.checksum = None
    for nm in args.file:
        if not isfile(nm):
            continue
        with open(nm, 'rb') as f:
            data = f.read()
        hexdat = sha256(data).hexdigest()
        print('SHA256 ({}) = {}'.format(nm, hexdat), end='')
        if args.checksum:
            if args.checksum != hexdat:
                print(' [ Failed ]', end='')
            else:
                print(' [ OK ]', end='')
        print()


if __name__ == '__main__':
    main(argv[1:])
