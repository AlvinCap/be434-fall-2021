#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-11-10
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('inputvalue',
                        help='A readable text/file',
                        metavar=str,
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    inputv = args.inputvalue
    if os.path.exists(inputv) and os.path.isfile(inputv):
        input_type = 'f'
    else:
        input_type = 'text'
    if input_type == 'f':
        sequences = inputv.file.read().splitlines()
    else:
        seq = str(inputv)
        
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
