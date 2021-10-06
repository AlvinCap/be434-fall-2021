#!/usr/bin/env python3
"""
Author : Alvin Onyango <capalvin@localhost>
Date   : 2021-09-28
Purpose: Protein Translate
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--c',
                        '--codons',
                        help='Codon Table for Translate',
                        metavar='Codons', nargs='*',
                        type=argparse.FileType('rt'))

    parser.add_argument('--o',
                    '--output',
                    help='Output File',
                    type=argparse.FileType('wt'))
                    
    parser.add_argument('--s',
                    '--sequence',
                    help='The string sequence',
                    metavar='str',
                    type=str,
                    default=None)
                        
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print(args)
# -----------------------------------------------
if __name__ == '__main__':
    main()
