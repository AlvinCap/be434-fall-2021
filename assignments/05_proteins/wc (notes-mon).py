#!/usr/bin/env python3
"""
Author : Alvin Onyango <capalvin@localhost>
Date   : 2021-09-28
Purpose: Counting Words
"""
import argparse
import sys
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Word Count',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable input file(s)',
                        metavar='File',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    total_lines = 0 
    total_words = 0 
    total_chars = 0

    for fh in args.files:
        num_lines = 0
        num_words = 0
        num_char = 0
        for line in fh:
            num_lines += 1
            num_words += (len(line.split()))
            num_char += len(line)
        print('{:>8}{:>8}{:>8} {}'.format(num_lines, num_words, num_char, fh.name))
        total_lines += num_lines 
        total_words += num_words 
        total_chars += num_char

    if len(args.files) >1: 
        print('{:>8}{:>8}{:>8} total'.format(total_lines, total_words, total_chars))
# -----------------------------------------------
if __name__ == '__main__':
    main()
