#!/usr/bin/env python3
"""
Author : Alvin Onyango <capalvin@localhost>
Date   : 2021-09-28
Purpose: Concatenate Files
"""
import argparse
# --------------------------------------------------


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Cat Files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable input file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='A Boolean Flag to Number Lines (default: False)',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for fh in args.files:
        line_num = 0
        for line in fh:
            line_num += 1
            if args.number:
                print("{:>6}\t{}".format(line_num, line.rstrip()))
            else:
                print(line.rstrip())


# -----------------------------------------------
if __name__ == '__main__':
    main()
