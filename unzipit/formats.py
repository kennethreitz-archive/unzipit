# -*- coding: utf-8 -*-

exts = {
    'tar.bz2':  ['tar -xj'],
    'tar.gz':   ['tar -xz'],
    'tar.7z':   ['7z x', 'tar -x'],
    'tar.lzo':  ['tar -x --lzop'],
    'tar.lzma': ['tar -x --lzma'],
    'tar.lz':   ['tar -x -lzip'],
    'tar.xz':   ['tar -x --xv'],
    'tar.Z':    ['tar -xZ'],
    'tar':      ['tar -x']
}
