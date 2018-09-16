def HammingDistance(string1,string2):
    hammingDist = 0
    for i in range(0,len(string1)):
        if string1[i] != string2[i]:
            hammingDist += 1
    return hammingDist

data = open('rosalind_hamm.txt').readlines()
print(HammingDistance(data[0], data[1]))


