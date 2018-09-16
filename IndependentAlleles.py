# Probability that offspring will have genotype AaBb is 0.25
# no matter the genotype that mates with the AaBb parent
# this makes this problem a binomial distribution problem


# Probability at least N AaBb organisms after k generations

import math


def ProbabilityAaBb(k,N):
    final_population = 2**k
    probabilityAaBb = 0
    for i in range (N, final_population+1):
        prob = (math.factorial(final_population) /
            (math.factorial(i) * math.factorial(final_population - i)))*(0.25**i) * (0.75**(final_population - i))
        probabilityAaBb += prob
    return probabilityAaBb

print(ProbabilityAaBb(7,33))