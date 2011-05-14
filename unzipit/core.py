# -*- coding: utf-8 -*-

import plac
from os import system

from unzipit import formats


@plac.annotations(fname='path to archive')
def main(fname, *test):
    ext = fname.split('.', 1)[1]

    if ext in formats.exts:
        for i, cmd in enumerate(formats.exts[ext]):
            fname = fname.rsplit('.', i)[0]
            print '%s %s' % (cmd, fname)
            #system('%s %s' % (cmd, fname))
    else:
        print('Archive must have a recognizable extension.')


def run():
    plac.call(main)
