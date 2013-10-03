#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vcf-venn.py
#  
#  Copyright 2013    Simon Gladman <simon.gladman@monash.edu>
#                    Charlotte Anderson <charlotte.anderson@unimelb.edu.au>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#   

#########
#imports#
#########

import sys
import itertools
import doctest
import argparse

parser = argparse.ArgumentParser()


parser.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE", required=True, action='append')
parser.add_argument("-p", "--prefix", dest="pref", help="prefix for output vcf name", metavar="string", required=True)
parser.add_argument("-d", "--dir", dest="out_dir", default="venn_results/", help="Output directory name", metavar="string")

args = parser.parse_args()

if len(args.filename) < 2:
  raise argparse.ArgumentTypeError("This program requires at least 2 files")

#############
#subroutines#
#############

def make_file_dictionary(file_list):
    '''
    subroutine to create and return a dictionary of the supplied file_list
    using an integer from 1 to len(file_list) as the keys
    
    >>>make_file_dictionary(['file_1','file2','file_3'])
    {1: 'file_1', 2: 'file_2', 3: 'file_3'}
    
    '''
    file_dict = {}
    file_count = 0
    for i in file_list:
        file_count += 1
        file_dict[file_count] = i
    return file_dict

def make_file_combinations(num_files):
    '''
    subroutine to make a list of file combinations (as lists) for the number of files
    supplied as the parameter. Returns a list of lists
    
    >>>make_file_combinations(3)
    [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    '''
    combos = []
    fns = xrange(1,num_files+1)
    for i in fns:
        x = itertools.combinations(fns, i)
        for j in x:
            combos.append(list(j))
    return combos


######
#main#
######

def main():
    
    return 0

if __name__ == '__main__':
    main()

