#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import glob
import json
import traceback
import os


def rewrite(fobj):
    text = json.load(fobj)
    clean = json.dumps(text, indent=4, sort_keys=True, separators=(',', ': ')) + '\n'
    fobj.seek(0)
    fobj.write(clean)
    fobj.truncate()

if __name__ == '__main__':
    DESCRIPTION = """
    Rewrites JSON configuration files for developers of intelmq.

    Corrections:
        Indentation, sorting, separators
    """
    parser = argparse.ArgumentParser(prog='rewrite_config_files.py',
                                     description="Test files")
    parser.add_argument('-c', '--config',
                        help='Path to the intelmq directory containing'
                             'bots/BOTS, etc/*.conf',
                        default='.')
    args = parser.parse_args()

    config_file_path = args.config

    try:
        for fn in glob.glob(os.path.join(config_file_path, 'etc/*.conf')):
            with open(fn, 'r+') as f:
                rewrite(f)

        with open(os.path.join(config_file_path, 'bots/BOTS'), 'r+') as f:
            rewrite(f)
    except IOError:
        traceback.print_exc()
        print('Could not open files. Wrong directory? Also see the --help.')