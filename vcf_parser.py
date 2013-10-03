######
#main#
######

def vcf_parser(file_dict):
    compare_dict={}
    for key, value in file_dict.iteritems():
      print key, value
      file=open(value, 'r')
      for line in file:
	if line.startswith('#'):
	  _header=line
	else:
	  CHROM, POS, ID, REF,ALT = line.strip().split()[:5]
	  if CHROM.startswith("chr"):
	    #print CHROM
	    CHROM = CHROM.replace('chr', '')
	    #print CHROM
	  identifier=CHROM+":"+POS+":"+ALT
	  if compare_dict.has_key(identifier):
	    #print "has key"
	    compare_dict[identifier][0].append(key)
	    compare_dict[identifier][1].append(line.strip())
	    
	  else:
	    compare_dict[identifier] = []
	    compare_dict[identifier].extend([[],[]])
	    compare_dict[identifier][0].append(key)
	    compare_dict[identifier][1].append(line.strip())
    
    return compare_dict

    
    
if __name__ == '__main__':
    file_dict={1: 'AOCS_137.Somatic.HighConfidenceConsequence.snv.vcf', 2: 'AOCS_137.test1.Somatic.HighConfidenceConsequence.snv.vcf', 3: 'AOCS_137.test2.Somatic.HighConfidenceConsequence.snv.vcf'}
    print file_dict
    print vcf_parser(file_dict)