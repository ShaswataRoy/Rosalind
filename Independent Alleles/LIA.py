import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

f = open(args.file,"r")
args = f.readline().split(" ")

k = int(args[0])
N = int(args[1])

p_d = 0.
p_h = 1.
p_r = 0.

for i in range(k):
    p_d,p_h,p_r = p_d*0.5 + p_h*0.25,p_d*0.5 + p_h*0.5 + p_r*0.5,p_r*0.5 + p_h*0.25

p_hh = p_h**2

p_cond = 0

for i in range(N, 2**k + 1):
    p_cond += math.comb(2**k,i)*p_hh**i*(1-p_hh)**(2**k-i)

with open("solution_lia.txt", "w") as text_file:
    text_file.write(str(p_cond))
