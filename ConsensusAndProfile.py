from Bio import SeqIO

fastaSequences = SeqIO.parse(open('input.txt','r'),'fasta')
seqIDs = []
dnaSequences = []
for record in fastaSequences:
    seqIDs.append(record.id)
    dnaSequences.append(str(record.seq))
    
#profile matrix is a list of length(sequence) consisting of lists of length 4
# each of the 4 values correspond to count of A, C, G, and T
profileMatrix = []
for i in range(0, len(dnaSequences[0])):
    profileMatrix.append([])
for i in range(0, len(profileMatrix)):
    for j in range(0,4):
        profileMatrix[i].append(0)
        
for i in range(0, len(profileMatrix)):
    for sequence in dnaSequences:
        if sequence[i] == 'A':
            profileMatrix[i][0] += 1
        elif sequence[i] == 'C':
            profileMatrix[i][1] += 1
        elif sequence[i] == 'G':
            profileMatrix[i][2] += 1
        elif sequence[i] == 'T':
            profileMatrix[i][3] += 1

#make  and print consensus string
consensusString = ''
for i in range (len(profileMatrix)):
    maxIndex = profileMatrix[i].index(max(profileMatrix[i]))
    if maxIndex == 0:
        consensusString += 'A'
    if maxIndex == 1:
        consensusString += 'C'
    if maxIndex == 2:
        consensusString += 'G'
    if maxIndex == 3:
        consensusString += 'T'

print(consensusString)

aCount = 'A: '
cCount = 'C: '
gCount = 'G: '
tCount = 'T: '

for i in range(0, len(profileMatrix)):
    aCount = ' '.join([aCount, str(profileMatrix[i][0])])
    cCount = ' '.join([cCount, str(profileMatrix[i][1])])
    gCount = ' '.join([gCount, str(profileMatrix[i][2])])
    tCount = ' '.join([tCount, str(profileMatrix[i][3])])
    
print(aCount)
print(cCount)
print(gCount)
print(tCount)
        