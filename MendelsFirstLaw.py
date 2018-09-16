
with open('input.txt', 'r') as file:
    line = file.readline().split()
    k,m,n = [int(num) for num in line]
    
    class Individual(object):
        allele1 = ''
        allele2 = ''
        def __init__(self, allele1, allele2):
            self.allele1 = allele1
            self.allele2 = allele2

    def makeIndividual(allele1, allele2):
        individual = Individual(allele1, allele2)
        return individual
    
    def makePopulation(k,m,n):
        population = []
        for i in range(0,k):
            population.append(makeIndividual('D','D'))
        for i in range(0,m):
            population.append(makeIndividual('D','R'))
        for i in range(0,n):
            population.append(makeIndividual('R','R'))
        return population
    
    def makeBabies(population):
        babies = []
        for i in range(0,len(population)-1):
            for j in range(i+1,len(population)):
                babies.append(makeIndividual(population[i].allele1, population[j].allele1))
                babies.append(makeIndividual(population[i].allele1, population[j].allele2))
                babies.append(makeIndividual(population[i].allele2, population[j].allele1))
                babies.append(makeIndividual(population[i].allele2, population[j].allele2))
        return babies
    
    population = makePopulation(k,m,n)
    babies = makeBabies(population)
    
    domCount = 0
    for baby in babies:
        if baby.allele1 == 'D' or baby.allele2 == 'D':
            domCount += 1
    
    print(domCount/len(babies))
    
    
file.close()

