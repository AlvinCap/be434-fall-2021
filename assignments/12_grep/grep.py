#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-12-09
Purpose: Rock the Casbah
"""

import argparse
import sys
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('inputF',
                        help='Pattern File',
                        type=argparse.FileType('rt'))

    parser.add_argument('-outF',
                       '--output',
                       help='An output file',
                       metavar='FILE',
                       type=argparse.FileType('wt'),
                       default= sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
