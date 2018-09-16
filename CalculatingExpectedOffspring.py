def ExpectedOffspring(a,b,c,d,e,f):
    return (1.0*a + 1.0*b + 1.0*c + .75*d + 0.5*e + 0*f) * 2


line = open('input.txt','r').readline().split()

for i in range(0, len(line)):
    line[i] = int(line[i])

print(line)

a = line[0]
b = line[1]
c = line[2]
d = line[3]
e = line[4]
f = line[5]

print(ExpectedOffspring(a,b,c,d,e,f))