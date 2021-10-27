#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-10-20
Purpose: Rock the Casbah
"""

import argparse
import parser


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        metavar='FILE2',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='A named integer value greater than 0',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()
    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')
    return args

# --------------------------------------------------
def main():

    args = get_args()
    kmers1 = {}
    for word in args.file1.read().rstrip().split():
        for kmer in find_kmers(word, args.kmer):
            if kmer not in kmers1:
                kmers1[kmer] = 0
            kmers1[kmer] += 1
    # print(kmers1)
    kmers2 = {}
    for word in args.file2.read().rstrip().split():
        for kmer in find_kmers(word, args.kmer):
            if kmer not in kmers2:
                kmers2[kmer] = 0
            kmers2[kmer] += 1
    # print(kmers2)
    commonk = set(kmers1).intersection(set(kmers2))
    # print(commonk)
    for kmer in commonk: 
        print(kmer, kmers1[kmer], kmers2[kmer])

def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
