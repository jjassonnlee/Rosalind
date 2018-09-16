from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


sequences = []
handle = open('input.fasta','r')
for record in SeqIO.parse(handle,'fasta'):
    sequences.append(str(record.seq))
handle.close()


dna_seq = sequences[0]
introns = sequences[1:]


for i in range(0, len(introns)):
    dna_seq = dna_seq.replace(introns[i], '')


dna_seq = Seq(dna_seq)
print(dna_seq.translate(to_stop=True))

