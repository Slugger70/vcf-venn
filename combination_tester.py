#!/usr/bin/env python

import sys
import itertools
import doctest

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
	
	
list_of_files = sys.argv[1:]
print list_of_files

file_dictionary = make_file_dictionary(list_of_files)

file_combinations = make_file_combinations(len(list_of_files))

for i in file_combinations:
	print i

