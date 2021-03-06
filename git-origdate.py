#!/usr/bin/env python3
# file: git-origdate.py
# vim:fileencoding=utf-8:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2015-01-03 15:48:13 +0100
# Last modified: 2017-06-04 13:35:18 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to git-origdate.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/
"""Report when arguments were checked into git."""

import os.path
import subprocess
import sys

__version__ = '1.0.1'


def main(argv):
    """
    Entry point for git-origdate.

    Arguments:
        argv: Command line arguments.
    """
    if len(argv) == 1:
        binary = os.path.basename(argv[0])
        print("{} ver. {}".format(binary, __version__), file=sys.stderr)
        print("Usage: {} [file ...]".format(binary), file=sys.stderr)
        sys.exit(0)
    del argv[0]  # delete the name of the script.
    try:
        for fn in argv:
            args = ['git', 'log', '--diff-filter=A', '--format=%ai', '--', fn]
            date = subprocess.check_output(args, stderr=subprocess.PIPE)
            date = date.decode('utf-8').strip()
            print('{}: {}'.format(fn, date))
    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            print("Not a git repository! Exiting.")
        else:
            print("git error: '{}'. Exiting.".format())


if __name__ == '__main__':
    main(sys.argv)
