import itertools


content = []
with open('input.txt', 'r') as file:
    for line in file:
        content.append(line.strip())
        
        
alphabet = content[0].split(sep=' ')
n = int(content[1])
permutations = itertools.product(alphabet, repeat = n)
answer = []


for i,j in enumerate(list(permutations)):
    permutation = ''
    for item in j:
        permutation += str(item)
    answer.append(permutation)
    
    
answer = sorted(answer)

for i,j in enumerate(answer):
    print(j)