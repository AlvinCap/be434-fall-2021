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

    parser.add_argument('-c',
                        '--codons',
                        help='Codon Table for Translate',
                        metavar='Codons', nargs='*',
                        required=True,
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--output',
                        help='Output File',
                        type=argparse.FileType('wt'), default='out.txt')
                    
    parser.add_argument('sequence',
                        help='The string sequence',
                        metavar='str')
                        
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    
    
# -----------------------------------------------
if __name__ == '__main__':
    main()
