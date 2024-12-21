import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

codon_file = open("RNA codon table.txt","r")
codon_table = {}

for line in codon_file:
    codon = line.replace("\n","").split(" ")
    codon_id = codon[0]
    amino_acid = codon[1]
    codon_table[codon_id] = amino_acid

codon_file.close()

s = open(args.file,"r").read()

protein = ""
for i in range(0,len(s),3):
    codon = s[i:i+3]
    if codon_table[codon] == "Stop":
        break
    protein += codon_table[codon]

with open("solution.txt", "w") as text_file:
    text_file.write(protein)


               