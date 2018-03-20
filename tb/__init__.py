# -*- coding: utf-8 -*-
## import
import sys
import re
import select
import argparse
from tabulate import tabulate

## def
def is_stdin():
    if select.select([sys.stdin,],[],[],0.0)[0]:
        return True
    return False

# to table format
def to_tbl(lines,args):
    tb_separator = args.separator + '+'
    tb_header = args.header
    tb_format = args.format

    tb_list = []
    for line in lines:
        line = line.rstrip()
        tb_list.append(re.split(tb_separator,line))
    print(tabulate(tb_list,tablefmt=tb_format,headers=tb_header))

def main():
    parser = argparse.ArgumentParser(description='Table making from list.')
    parser.add_argument('-s', '--separator', default=' ', type=str, help='Specify a set of characters to be used to delimit columns.')
    parser.add_argument('-l', '--header', default='', choices=['keys','firstrow'], help='table header')
    parser.add_argument('-f', '--format', default='orgtbl', choices=['simple','orgtbl','plain','grid','fancy-grid','pipe','jira','mediawiki','html','latex'],type=str, help='table format.')
    if is_stdin():
        args = parser.parse_args()
        lines = sys.stdin.readlines()
    else:
        parser.add_argument('file_path', action='store', type=str, help='file')
        args = parser.parse_args()
        lines = open(args.file_path,'r').readlines()
    to_tbl(lines,args)

if __name__ == '__main__': main()
