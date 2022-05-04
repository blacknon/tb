# -*- coding: utf-8 -*-
# Copyright(c) 2019 Blacknon. All rights reserved.
# Use of this source code is governed by an MIT license
# that can be found in the LICENSE file.

# TODO(blacknon): 標準入力から受け付けるよう修正する
# TODO(blacknon): 指定した配列をヘッダにするオプションを追加

import sys
import re
import select
import argparse
from tabulate import tabulate


# def
def is_stdin():
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        return True
    return False


# to table format
def to_tbl(lines, args):
    tb_separator = args.separator + '+'
    tb_header = args.header
    tb_format = args.format

    if args.article is False:
        tb_list = []
        for line in lines:
            line = line.rstrip()
            tb_list.append(re.split(tb_separator, line))
        print(tabulate(tb_list, tablefmt=tb_format, headers=tb_header))
    else:
        tb_list = []
        i = -1
        b_lenght = 0
        for line in lines:
            line = line.rstrip()
            line_array = re.split(tb_separator, line)
            length = len(line_array)
            if b_lenght != length or length < 2:
                i = i + 1
                tb_list.insert(i, [])
            tb_list[i].append(line_array)
            b_lenght = len(line_array)

        x = 0
        for e in tb_list:
            if len(e) == 1:
                if len(e[0][0]) == 0:
                    string = ''
                else:
                    string = lines[x]
                print(string.rstrip())
                x += 1
            else:
                print(tabulate(e, tablefmt=tb_format, headers=tb_header))
                x += len(e) + 1


def main():
    parser = argparse.ArgumentParser(description='Table making from list.')
    parser.add_argument('-s', '--separator', default=' ', type=str,
                        help='Specify a set of characters to be used to delimited columns.')
    parser.add_argument('-l', '--header', default='',
                        choices=['keys', 'firstrow'], help='table header')

    parser.add_argument('-f', '--format', default='orgtbl',
                        choices=[
                            'simple', 'orgtbl', 'github', 'plain', 'grid',
                            'fancy-grid', 'pipe', 'jira', 'mediawiki',
                            'html', 'latex'
                        ],
                        type=str, help='table format.')
    parser.add_argument('--article', dest='article',
                        default=False, action='store_true',
                        help='article flag')

    if is_stdin():
        args = parser.parse_args()
        lines = sys.stdin.readlines()
    else:
        parser.add_argument('file_path', action='store', type=str, help='file')
        args = parser.parse_args()
        lines = open(args.file_path, 'r').readlines()
    to_tbl(lines, args)


if __name__ == '__main__':
    main()
