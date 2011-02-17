# -*- coding: utf-8 -*-

import plac
from os import system

@plac.annotations(fname='path to archive')
def main(fname, *test):

    exts = fname.split('.')[1:]

    flags = ['x']

    if len(exts):
        if 'bz' in exts:
            flags.append('j')
        elif 'gz' in exts:
            flags.append('z')
        elif 'xz' in exts:
            flags.append('J')

        print 'tar -%s %s' % (''.join(flags), fname)

    else:
        print('Archive must have a recognizable extension.')




    # system('tar %s %s' % (flags, fname))

def run():
    plac.call(main)
