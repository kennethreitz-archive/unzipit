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
        if 'gz' in exts:
            flags.append('z')
        
        print 'tar -%s %s' % (''.join(flags), fname)
        
    else:
        print('Archive must have a recognizable extension.')
    
    
    
    
    # system('tar %s %s' % (flags, fname))

def run():
    plac.call(main)