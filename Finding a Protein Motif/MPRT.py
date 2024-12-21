from Bio import SeqIO
import requests
from io import StringIO 
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default="")
args = parser.parse_args()

with open(args.file,"r") as f:
    for seq_id in f:

        # Uniprot Protein ID read from fasta file
        seq_id = seq_id.replace("\n","")
        response = requests.get("http://www.uniprot.org/uniprot/" + seq_id.split("_")[0] + ".fasta")
        
        record_id = ''
        seq = ''

        # Read the fasta file
        for record in SeqIO.parse(StringIO(response.text), "fasta"):
            record_id = str(record.id)
            seq = str(record.seq)
        
        # Lookahead assertion allows overlapping matches
        glycosylation_motif = r'(?=N[^P][S|T][^P])'

        # Check if motif exists
        if re.search(glycosylation_motif, seq) is None:
            continue

        # Find all motif occurrences
        matches = re.finditer(glycosylation_motif, seq)

        print(seq_id)

        positions = []
        for match in matches:
            positions.append(match.span()[0]+1)

        if len(positions) > 0:
            print(" ".join(map(str, positions)))