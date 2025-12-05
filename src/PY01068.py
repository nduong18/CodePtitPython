from itertools import *
n,k = map(int, input().split())
a = input().split()
a = sorted(set(a))
for i in combinations(a,k):
    print(" ".join(i))