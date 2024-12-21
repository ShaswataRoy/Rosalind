from Bio import SeqIO

GC_contents = []
sequence_ids = []

# Calculate GC content of sequence
def GC_content(sequence):
    GC = 0
    for base in sequence:
        if base == "G" or base == "C":
            GC += 1
    return (GC / len(sequence)) * 100

# Parse the FASTA file
for record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    sequence_ids.append(record.id)
    GC_contents.append(GC_content(record.seq))

print(sequence_ids[GC_contents.index(max(GC_contents))])
print(max(GC_contents))
