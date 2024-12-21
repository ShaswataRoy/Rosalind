from Bio import SeqIO

ids = []
sequences = []

# Parse the FASTA file
for record in SeqIO.parse("rosalind_grph.txt", "fasta"):
    ids.append(record.id)
    sequences.append(record.seq)

k = len(sequences)

with open("solution_grph.txt", "w") as text_file:
    for i in range(k):
        for j in range(k):
            if i != j:
                if sequences[i][-3:] == sequences[j][:3]:
                    text_file.write(ids[i] + " " + ids[j] + "\n")