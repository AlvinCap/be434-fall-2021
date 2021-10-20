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
            elif element == 'C':
                newValue += "C"
            elif element == 'G':
                newValue += "G"
            elif element == 'T':
                newValue += "T"
            elif element == 'U':
                newValue += "U"
            elif element == 'R':
                newValue += "[AG]"
            elif element == 'Y':
                newValue += "[CT]"
            elif element == 'S':
                newValue += "[GC]"
            elif element == 'W':
                newValue += "[AT]"
            elif element == 'K':
                newValue += "[GT]"
            elif element == 'M':
                newValue += "[AC]"
            elif element == 'B':
                newValue += "[CGT]"
            elif element == 'D':
                newValue += "[AGT]"
            elif element == 'H':
                newValue += "[ACT]"
            elif element == 'V':
                newValue += "[ACG]"
            elif element == 'N':
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
