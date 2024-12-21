import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--n_months', type=str, default="",help="Number of months")
parser.add_argument('-k', '--k_pairs', type=str, default="",help="Number of pairs")
args = parser.parse_args()

n = int(args.n_months)
k = int(args.k_pairs)

adult = 0
offspring = 1

for i in range(1,n):
    adult,offspring = adult+offspring,adult*k

print(adult+offspring)