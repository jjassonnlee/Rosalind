def MortalFibRabbits(n, m):
    #mortalFib is fibonacci list of lists where index[0] is babyCount and index[1] is adultCount
    mortalFib = [1,1]
    for i in range(2,n):
        mortalFib.append(0)
    for i in range(2,n):
        if (i < m) or (m == 0):
            mortalFib[i] += mortalFib[i-1] + mortalFib[i-2]
        elif i == m:
            mortalFib[i] += mortalFib[i-1] + mortalFib[i-2] - 1
        elif i > m:
            mortalFib[i] += mortalFib[i-1] + mortalFib[i-2] - mortalFib[i-m-1]
    return mortalFib

print(MortalFibRabbits(89,18)[-1])