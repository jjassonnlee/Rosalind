def CountNucleotides(dnaSequence):
    count = [0, 0, 0, 0]
    for nucleotide in dnaSequence:
        if nucleotide == 'A':
            count[0] += 1
        elif nucleotide == 'C':
            count[1] += 1
        elif nucleotide == 'G':
            count[2] += 1
        elif nucleotide == 'T':
            count[3] += 1
    return count

data = open('input.txt')
data = data.readlines()
data = data[0].replace('\n', '')

count = CountNucleotides(data)

print(count)

print (' '.join(map(str, count)))