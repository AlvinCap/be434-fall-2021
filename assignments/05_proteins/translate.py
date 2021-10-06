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
                        metavar='Codons', 
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
    seq = args.sequence
    inFile = args.codons
    outFile = args.output

    CodonT = {}
    for line in inFile:
        key, value = line.rstrip().split() 
        CodonT[key] = value
    k = 3
    sequenceP = [] 
    for kmer in [seq[i:i + k] for i in range(0, len(seq), k)]:
        sequenceP.append(CodonT.get(kmer.upper(), '-'))
    outFile.write(''.join(sequenceP))
    outFile.close()
    print('Output written to "{}".'.format(outFile.name))

    

        
    
    
    
# -----------------------------------------------
if __name__ == '__main__':
    main()
