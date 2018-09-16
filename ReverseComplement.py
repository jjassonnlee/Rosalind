def ReverseComplement(dna):
    dna = dna[::-1]
    revC = ''
    complement = {'A': 'T',
                  'C': 'G',
                  'G': 'C',
                  'T': 'A'}
    for nucleotide in dna:
        revC = revC + complement[nucleotide]
    return revC

data = open('input.txt')
data = data.readlines()
data = data[0].replace('\n', '')

print(ReverseComplement(data))
