import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--DNA', type=str, default="")
args = parser.parse_args()

DNA_string = args.DNA

A_count = 0
C_count = 0
G_count = 0
T_count = 0

for nucleobase in DNA_string:
    if nucleobase == "A":
        A_count += 1
    elif nucleobase == "C":
        C_count += 1
    elif nucleobase == "G":
        G_count += 1
    elif nucleobase == "T":
        T_count += 1

print(A_count, C_count, G_count, T_count)