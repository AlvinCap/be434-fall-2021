#!/usr/bin/env python3
"""
Author : Alvin Onyango <capalvin@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integers',
                        help='Sum of Numbers',
                        metavar='int',
                        type=int,
                        nargs='+')
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    numList = args.nums
    print('{} = {}'.format('+'.join(map(str, numList)), sum(numList)))
# --------------------------------------------------
if __name__ == '__main__':
    main()