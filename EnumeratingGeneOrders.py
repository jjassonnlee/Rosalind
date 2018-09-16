import math
import itertools


n = 6
print(math.factorial(n))
permutations = itertools.permutations((range(1, n+1)))

for i,j in enumerate(permutations):
    permutation = ''
    for item in j:
        permutation += str(item) + ' '
    print(permutation)