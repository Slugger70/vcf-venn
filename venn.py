import argparse

parser = argparse.ArgumentParser()

#usage = "usage: %prog  arg1 arg2"
#parser = argparse.ArgumentParser(usage=usage)

parser.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE", required=True, action='append')
parser.add_argument("-p", "--prefix", dest="pref", help="prefix for output vcf name", metavar="string", required=True)
parser.add_argument("-d", "--dir", dest="out_dir", default="venn_results/", help="Output directory name", metavar="string")

args = parser.parse_args()

if len(args.filename) < 2:
  raise argparse.ArgumentTypeError("This program requires at least 2 files")