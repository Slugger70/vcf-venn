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
import os
import datetime

#################
#parse arguments#
#################

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE", required=True, action='append')
parser.add_argument("-p", "--prefix", dest="pref", help="prefix for output vcf name", metavar="string", required=True)
parser.add_argument("-d", "--dir", dest="out_dir", default="venn_results", help="Output directory name", metavar="string")

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

#-----------------------------------------------------

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

#-----------------------------------------------------

def vcf_parser(file_dict):
    '''
    subroutine to take in a file dictionary (keyed by an integer)
    and parse each file in turn into a vcf_dictionary. The vcf_dict
    is structured as follows:
        Key - chromosome:postion:altAllele (separator “:”)
        value - array:  [0]: a list of file numbers in which this snv occurs
                        [1]: the vcf line in file if the same, no meta-data if different (cut down line instead)
    
    Tests:
    Could be very hard to do in here! We will need some other test mechanism
    
    '''
    compare_dict={}
    header = []
    for key, value in file_dict.iteritems():
      print key, value
      file=open(value, 'r')
      for line in file:
	if line.startswith('#'):
	  if "<" in line:
	    header.append(line)
	else:
	  if line.startswith("chr"):
        #print line
	    line = line.replace('chr', '')
	    #print CHROM
	  CHROM, POS, ID, REF,ALT = line.strip().split()[:5]
	  identifier=CHROM+":"+POS+":"+ALT
	  if compare_dict.has_key(identifier):
	    #print "has key"
	    compare_dict[identifier][0].append(key)
	    #print compare_dict[identifier][1][0]
	    if line == compare_dict[identifier][1][0]:
	    	_sameLine =1
	    	#print "same"
	    else:
	    	#compare_dict[identifier][1].append(line)
	    	#print "remove meta data"
	    	new_line = CHROM+"\t"+POS+"\t"+ID+"\t"+REF+"\t"+ALT+"\t.\t.\t.\t.\t.\n"
	    	#print new_line
	    	compare_dict[identifier][1] = []
	    	compare_dict[identifier][1].append(new_line)
	    	
	    
	  else:
	    compare_dict[identifier] = []
	    compare_dict[identifier].extend([[],[]])
	    compare_dict[identifier][0].append(key)
	    compare_dict[identifier][1].append(line)
    #print compare_dict
    header = sorted(set(header))
    #print "".join([str(x) for x in header])
    return compare_dict, header

#-----------------------------------------------------

def vcf_combo_writer(prefix, directory, combo_list, compare_dict, header):
	'''
	subroutine which looks into comparison dictionary and writes vcf output
	files based on different combinations (combo list)
	'''
	for combination in combo_list:
		#print combination
		file=open(os.path.join(directory, prefix + "." + "V".join([str(x) for x in combination]) + ".vcf"), 'w')
		file.write("##fileformat=VCFv4.0\n")
		today = datetime.date.today()
		file.write("##fileDate="+today.strftime('%d%m%Y\n'))
		file.write("".join([str(x) for x in header]))
		file.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n")
		for val in compare_dict.values():
			combo, lines  = val
			if combo == combination:
				#print combo, combination
				if len(lines) > 1:
					print "need to compare the lines", lines
					_compare_lines = 0
				else:
					#print lines[0]
					file.write(lines[0])
		file.close()

#-----------------------------------------------------

def make_venn_output(combo_list, vcf_dict):
    '''
    Produces a dictionary of the filename combinations and the number of snvs unique to each 
    and returns it.
    '''
    count_dict = {}
    for i in combo_list:
        count_dict[str(i)] = 0
    
    for i in combo_list:
        for x in vcf_dict.values():
            combo,lines = x
            if combo == i:
                count_dict[str(i)] += 1
            
    #print count_dict
    return count_dict



######
#main#
######

def main():
    
    opening_lines = "************************************\nvcf-venn\n"
    opening_lines += "Arguments:\n"
    opening_lines += "\tfiles:\t"
    opening_lines += str(args.filename) + "\n"
    opening_lines += "\tprefix:\t" + args.pref + "\n"
    opening_lines += "\toutdir:\t" + args.out_dir + "\n"
    opening_lines += "************************************\n"
    
    sys.stderr.write(opening_lines)
    
    #we need to make sure the files exist!
    sys.stderr.write("Checking existence of input files\n")
    for i in args.filename:
        if not os.path.isfile(i):
            raise Exception("Filename " + i + " doesn't exist!")

    sys.stderr.write("Make output directory\n")
    #make the output directory checking for its existence first.
    if(os.path.isdir(args.out_dir)):
        raise Exception("Output directory already exists, will not overwrite. Exiting.")
    else:
        os.mkdir(args.out_dir)

    #first we need to make a dictionary of the list of files.
    #we use make_file_dictionary for this
    sys.stderr.write("Producing the file dictionary\n")
    file_dict = make_file_dictionary(args.filename)

    sys.stderr.write("Producing list of file combinations\n")
    #now we need to make the combinations list for the comparisons
    #and we give it the length of the filename arguement here
    combo_list = make_file_combinations(len(args.filename))

    sys.stderr.write("Parsing the vcf files\n")
    #parse the vcf files into the vcf_dictionary!
    vcf_dict, header = vcf_parser(file_dict)

    sys.stderr.write("Writing the venn diagram output\n")
    #make the venn output
    venn_out = make_venn_output(combo_list, vcf_dict)
    file = open(os.path.join(args.out_dir, "venn-out.txt"), "w")
    for c in venn_out:
        file.write(str(c) + "," + str(venn_out[c]) + "\n")
    file.close()

    sys.stderr.write("Writing the output files\n")
    #write the vcf files out
    vcf_combo_writer(args.pref, args.out_dir, combo_list, vcf_dict, header)

    return 0

if __name__ == '__main__':
    main()

