#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-10-06
Purpose: Common Words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Common Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input File 1',
                        metavar='FileOne',
                        type=argparse.FileType('rt'))
    parser.add_argument('file2',
                        help='Input File 2',
                        metavar='FileTwo',
                        type=argparse.FileType('rt'))
    parser.add_argument('-o',
                        '--output',
                        help='Output File',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1 = args.file1
    file2 = args.file2
    fileOut = args.output
    file1words = set(args.file1.read().rstrip().split())
    file2words = set(args.file2.read().rstrip().split())
    # for word in file1.read().split():
    #     file1words.add(word.lower())
    # for word in file2.read().split():
    #     file2words.add(word.lower())
    commonWords = list(file1words.intersection(file2words))
    commonWords.sort()
    print(*commonWords, sep="\n", file=fileOut)


# --------------------------------------------------
if __name__ == '__main__':
    main()
