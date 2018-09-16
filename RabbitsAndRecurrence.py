#n months, k offspring each month
def RabbitsAndRecurrence(n,k):
    fibRabbits = [1,1]
    for i in range(2,n):
        fibRabbits[i] = fibRabbits[i-1] + fibRabbits[i-2]*k
    return fibRabbits[-1]

def RecursiveFibRabbits(n,k):
    if n <= 2:
        return 1
    else:
        return RecursiveFibRabbits(n-1,k) + RecursiveFibRabbits(n-2,k)*k

print(RecursiveFibRabbits(34,4))