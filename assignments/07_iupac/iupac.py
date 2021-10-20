#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-10-13
Purpose: Translate Iupac
"""

import argparse
import sys

# import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='IUPAC Sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        help='Seq Position Argument',
                        nargs='+',
                        metavar='str')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output File',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    code = args.seq
    codeList = code
    outFile = args.outfile

    for value in codeList:
        newValue = value + ' '
        for element in value:
            if element == 'A':
                newValue += "A"
            if element == 'C':
                newValue += "C"
            if element == 'G':
                newValue += "G"
            if element == 'T':
                newValue += "T"
            if element == 'U':
                newValue += "U"
            if element == 'R':
                newValue += "[AG]"
            if element == 'Y':
                newValue += "[CT]"
            if element == 'S':
                newValue += "[GC]"
            if element == 'W':
                newValue += "[AT]"
            if element == 'K':
                newValue += "[GT]"
            if element == 'M':
                newValue += "[AC]"
            if element == 'B':
                newValue += "[CGT]"
            if element == 'D':
                newValue += "[AGT]"
            if element == 'H':
                newValue += "[ACT]"
            if element == 'V':
                newValue += "[ACG]"
            if element == 'N':
                newValue += "[ACGT]"
            else:
                newValue += ''
        if outFile == sys.stdout:
            print(newValue)
        else:
            outFile.write((newValue + '\n'))
    if outFile != sys.stdout:
        print('Done, see output in "{}"'.format(outFile.name))
        outFile.close()
    else:
        pass


# --------------------------------------------------
if __name__ == '__main__':
    main()
