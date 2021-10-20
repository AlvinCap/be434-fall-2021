#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-10-20
Purpose: Rock the Casbah
"""

import argparse



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='A named integer value greater than 0',
                        metavar='int',
                        type=int,
                        default=3)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.kmer <= 0:
        # return parser.error()
    # else: 
        # print(args.kmer)





# --------------------------------------------------
if __name__ == '__main__':
    main()
