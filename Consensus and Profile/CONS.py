from Bio import SeqIO
import numpy as np

sequence_matrix = []

# Calculate profile matrix
def profile_matrix(sequence_matrix):
    p_matrix = np.zeros((4, len(sequence_matrix[0])), dtype=int)
    for indx,col in enumerate(sequence_matrix.T):
        A = 0
        C = 0
        G = 0
        T = 0
        for base in col:
            if base == "A":
                A += 1
            elif base == "C":
                C += 1
            elif base == "G":
                G += 1
            elif base == "T":
                T += 1
        p_matrix[:, indx] = np.array([A, C, G, T])
    return p_matrix

# Parse the FASTA file
for record in SeqIO.parse("rosalind_cons.txt", "fasta"):
    sequence_matrix.append(record.seq)

sequence_matrix = np.array(sequence_matrix)
p_matrix = profile_matrix(sequence_matrix)

consensus = ""
for i in range(len(p_matrix[0])):
    consensus += "ACGT"[np.argmax(p_matrix[:, i])]

with open("solution.txt", "w") as text_file:
    text_file.write(consensus + "\n")
    for i, base in enumerate("ACGT"):
        text_file.write(base + ": " + " ".join(map(str, p_matrix[i])) + "\n")