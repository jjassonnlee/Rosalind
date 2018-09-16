from urllib.request import urlopen
from Bio import SeqIO
import re


proteinIDs = []
with open('input.txt','r') as file:
    for line in file:
        proteinIDs.append(line.strip())
file.close()
print(proteinIDs)

for i in range(len(proteinIDs)):
    URL = 'http://www.uniprot.org/uniprot/' + proteinIDs[i] + '.fasta'
    data = urlopen(URL)
    fasta = data.read().decode('utf-8', 'ignore')
    with open('seq_file.fasta','a') as text_file:
        text_file.write(fasta)


handle = open('seq_file.fasta','r')
motif = re.compile(r'(?=(N[^P][ST][^P]))')
count = 0


prot_seqs = []
for record in SeqIO.parse(handle,'fasta'):
    prot_seqs.append(str(record.seq))
handle.close()


for i in range(0, len(prot_seqs)):
    positions = []
    for match in re.finditer(motif, prot_seqs[i]):
        positions.append(match.start() + 1)
    if len(positions) > 0:
        print(proteinIDs[i])
        print(' '.join(map(str, positions)))
