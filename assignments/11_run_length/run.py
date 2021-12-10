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

    parser.add_argument('inputval',
                        help='A readable DNA text or file',
                        metavar=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    inputv = args.inputval
    if os.path.exists(inputv) and os.path.isfile(inputv):
        input_type = 'f'
        if input_type == 'f':
            sequences = open(file=inputv, mode='rt', encoding='UTF-8')
            seqfile = (sequences.readlines())
            print(seqfile)
        else:
            seq = (inputv)
            print(seq)


# --------------------------------------------------
if __name__ == '__main__':
    main()
