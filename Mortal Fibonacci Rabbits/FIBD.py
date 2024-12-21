import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

f = open(args.file,"r")
args = f.readline().split(" ")

n = int(args[0])
m = int(args[1])

# Number of rabbits of age i at time t --> ri
rabbits = np.zeros((n,m),dtype='i8')

for t in range(n):
    for i in range(m):
        if t == 0:
            if i == 0:
                rabbits[t][i] = 1
            else:
                rabbits[t][i] = 0
        else:
            if i == 0:
                rabbits[t][i] = sum(rabbits[t-1][1:])
            else:
                rabbits[t][i] = rabbits[t-1][i-1]

with open("solution.txt", "w") as text_file:
    text_file.write(str(int(sum(rabbits[n-1]))))