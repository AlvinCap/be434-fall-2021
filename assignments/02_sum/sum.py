#!/usr/bin/env python3
"""
Author : Alvin Onyango <capalvin@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integers',
                        help='Sum of Numbers',
                        metavar='int',
                        type=int,
                        nargs='+')
    parser.add_argument('--sum',
                        dest='accumulate',
                        action='store_const',
                        const=sum,
                        default=sum,
                        help='sum the integers (default: find the max)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    numList = []
    args = get_args()
    for num in args.integers:
        numList.append(num)
    for num in numList:
        num = str(num)
    # print(numList)
    JoinList = []
    if len(numList) > 1:
        for element in (numList):
            JoinList.append(str(element))
        JoinS = ' + '.join(JoinList)
        print(JoinS, "=", (args.accumulate(args.integers)))

    else:
        print((args.accumulate(args.integers)), '=',
              (args.accumulate(args.integers)))


# --------------------------------------------------
if __name__ == '__main__':
    main()