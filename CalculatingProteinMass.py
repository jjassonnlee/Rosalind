from Bio.Seq import Seq
from Bio.Alphabet import generic_protein
from Bio.SeqUtils import molecular_weight


with open('input.txt','r') as file:
    for line in file:
        protein_seq = line.strip('\n')


print('%0.3f' % (molecular_weight(
        Seq(protein_seq, generic_protein),
        monoisotopic=True) - 18.01056))