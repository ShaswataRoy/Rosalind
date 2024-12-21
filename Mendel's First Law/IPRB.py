import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

f = open(args.file,"r")
args = f.readline().split(" ")

k = int(args[0])
m = int(args[1])
n = int(args[2])

total = k + m + n

p_rr = (n / total) * ((n - 1) / (total - 1))
p_rd = (n / total) * (m / (total - 1)) + (m / total) * (n / (total - 1))
p_dd = (m / total) * ((m - 1) / (total - 1))

p_r = p_rr + p_rd * 0.5 + p_dd * 0.25
p_d = 1 - p_r

print(p_d)