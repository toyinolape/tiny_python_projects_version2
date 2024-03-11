#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

   
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.text
    jumper_dict = {'1' : 9, '2' : 8, '3' : 7, '4' : 6, '5' : 0, '6' : 4, '7' : 3, '8' : 2, '9' : 1, '0' : 5}
    decode = ''
    for text in str_arg:
        if text in jumper_dict.keys():
            text = str(jumper_dict[text])

        else: 
            text = text

        decode += text  

    print(f'{decode}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
