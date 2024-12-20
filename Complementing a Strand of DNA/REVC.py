import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()


s = open(args.file,"r").read()
s_complement = s.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()
s_complement = s_complement[::-1]

print(s_complement)