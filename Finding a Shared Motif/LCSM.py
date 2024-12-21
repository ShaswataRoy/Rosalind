from Bio import SeqIO

ids = []
sequences = []

# Parse the FASTA file
for record in SeqIO.parse("rosalind_lcsm.txt", "fasta"):
    ids.append(record.id)
    sequences.append(str(record.seq))

n = len(sequences)
l = min([len(seq) for seq in sequences]) # Length of the shortest sequence, used to keep algorithm short. Common sequence will be in this sequence.
min_index = sequences.index(min(sequences, key=len)) # Index of the shortest sequence
common_seq = []

for i in range(l):
    for j in range(i):
        exist = True # Flag to check if a common sequence is found in all sequences
        for k in range(n):
            if sequences[min_index][j:i] not in sequences[k]:
                exist = False
                break
        if exist:
            common_seq.append(sequences[min_index][j:i])
            break # If a common sequence is found, break the loop since we are looking for the longest common sequence  


with open("solution_lcsm.txt", "w") as text_file:
    text_file.write(max(common_seq,key=len))