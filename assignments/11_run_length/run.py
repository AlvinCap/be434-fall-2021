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

    parser.add_argument('text',
                        help='Input Text or File Handle',
                        metavar='str')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for seq in args.text.splitlines():
        print(test_rle(seq))


# --------------------------------------------------
def test_rle(seq: str) -> str:
    countsVal = []
    count = 0
    prev = ''
    for char in seq:
        if prev == '':
            prev = char
            count = 1
        elif char == prev:
            count += 1
        else:
            countsVal.append((prev, count))
            count = 1
            prev = char
    countsVal.append((prev, count))

    reg = ''
    for char, count in countsVal:
        reg += '{}{}'.format(char, count if count > 1 else '')

    return reg


# --------------------------------------------------
if __name__ == '__main__':
    main()
