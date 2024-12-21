import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

f = open(args.file,"r")
s = f.readline().strip()
t = f.readline().strip()

hamming_distance = 0

for indx in range(len(s)):
    if s[indx] != t[indx]:
        hamming_distance += 1

print(hamming_distance)

