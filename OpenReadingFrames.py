import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


record = SeqIO.read('input.fasta', 'fasta')
pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
forward_seq = record.seq
reverse_seq = forward_seq.reverse_complement()
sequences = []


for match in re.findall(pattern, str(forward_seq)):
    dna_seq = Seq(match, generic_dna)
    prot_seq = dna_seq.translate()
    if prot_seq not in sequences:
        sequences.append(prot_seq)
        
for match in re.findall(pattern, str(reverse_seq)):
    dna_seq = Seq(match, generic_dna)
    prot_seq = dna_seq.translate()
    if prot_seq not in sequences:
        sequences.append(prot_seq)
        

for i,s in enumerate(sequences):
    print(s)
