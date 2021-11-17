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

    parser.add_argument('input',
                        help='A readable text/file',
                        metavar=str,
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    input = args.input
    if os.path.exists(input)

    



# --------------------------------------------------
if __name__ == '__main__':
    main()
