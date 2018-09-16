from Bio import SeqIO

fastaSequences = SeqIO.parse(open('rosalind_gc.fasta'),'fasta')
seqIDs = []
sequences = []
for record in fastaSequences:
    seqIDs.append(record.id)
    sequences.append(str(record.seq))


def GCContent(dna):
    count = 0
    for nucleotide in dna:
        if nucleotide == 'G' or nucleotide == 'C':
            count += 1
    return count/len(dna)


maxSeqID = ''
maxPercentage = 0
for i in range(0,len(sequences)):
    if GCContent(sequences[i]) > maxPercentage:
        maxPercentage = GCContent(sequences[i])
        maxSeqID = seqIDs[i]

print(maxSeqID)
print(maxPercentage * 100)
