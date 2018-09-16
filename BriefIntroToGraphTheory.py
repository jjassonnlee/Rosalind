from Bio import SeqIO

fastaSequences = SeqIO.parse(open('rosalind_grph.txt','r'),'fasta')
seqIDs = []
dnaSequences = []
for record in fastaSequences:
    seqIDs.append(record.id)
    dnaSequences.append(str(record.seq))
    
adjacencyList = []

for i in range(0, len(dnaSequences)-1):
    for j in range (i+1, len(dnaSequences)):
        if dnaSequences[i] != dnaSequences[j]:
            if (dnaSequences[i][0:3] == dnaSequences[j][-3:]):
                adjacencyList.append(seqIDs[j] + ' ' + seqIDs[i])
            elif (dnaSequences[i][-3:] == dnaSequences[j][0:3]):
                adjacencyList.append(seqIDs[i] + ' ' + seqIDs[j])

file = open('answer.txt','w+')

for item in adjacencyList:
    file.write(item + '\n')

file.close()

