#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from commands import getoutput as get_output

import clint
from clint.textui import colored, puts, indent

from .formats import filename_to_commands

def show_usage():
    """Shows CLI Usage."""

    print '{0} by Kenneth Reitz <me@kennethreitz.com>'.format(
        colored.yellow('unzipit')
    )
    print 'https://github.com/kennethreitz/unzipit\n'
    print 'Usage: {0}'.format(colored.cyan('unzipit <in-file>'))


def main():
    """CLI Dispatch."""

    if not len(clint.args.files):
        show_usage()
        sys.exit(1)

    in_file = clint.args.files.pop()

    chain = filename_to_commands(in_file)

    if len(chain) is 1:
        cmd = chain.pop().format(in_file)

        puts('{0}:\n'.format(colored.blue(cmd)))

        os.system(cmd)


    elif len(chain) is 2:
        print chain
        # print chain.pop().format(in_file)


if __name__ == '__main__':
    main()