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

#################
#parse arguments#
#################

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

def vcf_parser(file_dict):
    '''
    subroutine to take in a file dictionary (keyed by an integer)
    and parse each file in turn into a vcf_dictionary. The vcf_dict
    is structured as follows:
        Key - chromosome:postion:altAllele (separator “:”)
        value - array:  [0]: a list of file numbers in which this snv occurs
                        [1]: the vcf line in file if the same, no meta-data if different (cut down line instead)
    
    Tests:
    
    
    '''
    pass

def vcf_combo_writer(out_prefix, out_dir, combo_list, vcf_dict):
    '''
    
    '''
    pass

def make_venn_output(combo_list, vcf_dict):
    '''
    
    '''
    pass

######
#main#
######

def main():
    
    #first we need to make a dictionary of the list of files.
    #we use make_file_dictionary for this
    file_dict = make_file_dictionary(args.filename)
    
    #now we need to make the combinations list for the comparisons
    #and we give it the length of the filename arguement here
    combo_list = make_file_combinations(len(args.filename))
    
    #parse the vcf files into the vcf_dictionary!
    vcf_dict = vcf_parser(file_dict)
    
    #make the venn output
    venn_out = make_venn_output(combo_list, vcf_dict)
    
    #write the vcf files out
    vcf_combo_writer(out_prefix, out_dir, combo_list, vcf_dict)
    
    return 0

if __name__ == '__main__':
    main()

