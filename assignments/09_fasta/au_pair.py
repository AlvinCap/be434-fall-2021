#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-11-01
Purpose: Rock the Casbah
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        nargs='+',
                        help='Input File(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outFile',
                        help='A output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outF = args.outFile
    if not os.path.isdir(outF):
        os.makedirs(outF)
    for file in args.files:
        root, ext = os.path.splitext(os.path.basename(file.name))
        forward = open(os.path.join(outF, root + '_1' + ext), 'wt')
        reverse = open(os.path.join(outF, root + '_2' + ext), 'wt')
        parser = SeqIO.parse(file, 'fasta')
        for i, rec in enumerate(parser):
            SeqIO.write(rec, forward if i % 2 == 0 else reverse, 'fasta')
    print(f'Done, see output in "{outF}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
