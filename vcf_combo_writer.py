import os

def vcf_combo_write(prefix, directory, combo_list, compare_dict):
  
  
  for combination in combo_list:
    print combination
    file=open(os.path.join(directory, prefix + "." + "V".join([str(x) for x in combination]) + ".vcf"), 'w')
    for val in compare_dict.values():
      combo, lines  = val
      if len(combo) > 1:
	#print "need to compare the lines", combo
	_compare_lines = 0
      if combo == combination:
	#print combo, combination
	#print lines[0]
	file.write(lines[0])
	

    
    


    

if __name__ == '__main__':
  prefix = "test_results" 
  directory = "venn_results" 
  combo_list = [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
  compare_dict = {'7:48046851:G': [[1, 2, 3], ['7\t48046851\t.\tC\tG\t.\tBothFiles\tGENE=SUN3;TYPE=Missense_Mutation\tGT\t0/1\n', '7\t48046851\t.\tC\tG\t.\tBothFiles\tGENE=SUN3;TYPE=Missense_Mutation\tGT\t0/1', '7\t48046851\t.\tC\tG\t.\tBothFiles\tGENE=SUN3;TYPE=Missense_Mutation\tGT\t0/1']], '9:104152897:T': [[1, 2, 3], ['9\t104152897\t.\tG\tT\t.\tBothFiles\tGENE=MRPL50;TYPE=Missense_Mutation\tGT\t0/1\n', '9\t104152897\t.\tG\tT\t.\tBothFiles\tGENE=MRPL50;TYPE=Missense_Mutation\tGT\t0/1', '9\t104152897\t.\tG\tT\t.\tBothFiles\tGENE=MRPL50;TYPE=Missense_Mutation\tGT\t0/1']], '16:66948151:C': [[1, 2], ['16\t66948151\t.\tG\tC\t.\tBothFiles\tGENE=CDH16;TYPE=Missense_Mutation\tGT\t0/1\n', '16\t66948151\t.\tG\tC\t.\tBothFiles\tGENE=CDH16;TYPE=Missense_Mutation\tGT\t0/1']]}
  print vcf_combo_write(prefix, directory, combo_list, compare_dict)