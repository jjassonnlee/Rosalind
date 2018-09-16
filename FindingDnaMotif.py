def FindMotifs(dna,motif):
    motifLocations = []
    for i in range(0,len(dna)-len(motif)):
        if dna[i:i+len(motif)] == motif:
            motifLocations.append(i+1)
    return motifLocations

with open('input.txt','r') as file:
    data = file.read().splitlines()
    motifLocations = FindMotifs(data[0],data[1])
    for i in range(0,len(motifLocations)):
        motifLocations[i] = str(motifLocations[i])
    print(' '.join(motifLocations))

file.close()