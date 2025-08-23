import itertools
n = int(input())
r = ['A','B','C']
z = []

for i in range(3,n+1):
    l = list(itertools.permutations(r,i))
    z.append(l)

print(z)