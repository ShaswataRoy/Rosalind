import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

f = open(args.file,"r")
args = f.readline().split(" ")

n = []

for arg in args:
    n.append(int(arg))

# Vector of probabilities corresponding to each case
p = [1.,1.,1.,.75,0.5,0.]

# Expected number of offspring with dominant phenotype
E = 0

for i in range(6):
    E += 2*n[i]*p[i]

with open("solution_iev.txt", "w") as text_file:
    text_file.write(str(E))