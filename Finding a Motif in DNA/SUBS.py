import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

f = open(args.file,"r")
s = f.readline().strip()
t = f.readline().strip()

repeat_indices = []
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        repeat_indices.append(i+1)

print(" ".join(map(str,repeat_indices)))