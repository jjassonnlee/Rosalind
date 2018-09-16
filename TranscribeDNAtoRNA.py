def Transcribe(dna):
    return dna.replace('T', 'U')

data = open('input.txt')
data = data.readlines()
data = data[0].replace('\n', '')

rna = Transcribe(data)
print (rna)