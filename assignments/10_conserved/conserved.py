#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-11-17
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input seuquence',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args)

    charseq = args.file.read().splitlines()

    print('\n'.join(charseq))

    for i in range(len(charseq[0])):
        bases = []
        for element in charseq:
            bases.append(element[i])
        # print(bases)
        if all([bases[0] == base for base in bases]):
            print('|', end='')
        else:
            print('X', end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
