#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-10-13
Purpose: Translate Iupac
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='IUPAC Sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        help='A positional argument',
                        nargs='+',
                        metavar='str')
    
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
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
