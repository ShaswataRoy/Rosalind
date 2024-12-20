import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

t = open(args.file,"r").read()

r = t.replace("T", "U")

print(r)