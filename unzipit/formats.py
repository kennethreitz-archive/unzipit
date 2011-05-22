# -*- coding: utf-8 -*-

expand_map = {
    'tar.bz2':
        ['tar xvjf {0}'],
    'tar.gz':
        ['tar xvzf {0}'],
    'tgz':
        ['tar xvzf {0}'],
    'tar.7z':
        ['7z x {0}', 'tar -x'],
    'tar.lzo':
        ['tar -x --lzop {0}'],
    'tar.lzma':
        ['tar -x --lzma {0}'],
    'tar.lz':
        ['tar -x -lzip {0}'],
    'tar.xz':
        ['tar -x --xv {0}'],
    'tar.Z':
        ['tar -xZ {0}'],
    'tar':
        ['tar xvf {0}'],
    'zip':
        ['unzip -u {0}'],
    'egg':
        ['unzip -u {0}'],
    'jar':
        ['unzip -u {0}'],
    'gz':
        ['gunzip {0}'],
    'bz2':
        ['bunzip2 {0}']
}


def filename_to_commands(fname):
    """Returns a list of commands to expand a file."""

    for (extension, command_chain) in expand_map.items():
        if fname.endswith(extension):
            return command_chain