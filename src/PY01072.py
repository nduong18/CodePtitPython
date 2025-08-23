import itertools
n,k = map(int,input().split())
x = sorted(set(list(map(int,input().split()))))
y = list(itertools.combinations(x,k))
for i in y:
    print(*i)