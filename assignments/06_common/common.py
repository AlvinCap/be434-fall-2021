#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-10-06
Purpose: Common Words
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Common Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input File 1',
                        metavar='FileOne',
                        required=True, type=argparse.FileType('rt'))
    parser.add_argument('file2',
                        help='Input File 2',
                        metavar='FileTwo',
                        required=True, type=argparse.FileType('rt'))
    parser.add_argument('-o',
                        '--output',
                        help='Output File',
                        type=argparse.FileType('wt'), default='out.txt')
                    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1 = args.file1
    file2 = args.file2
    fileOut = args.output
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
