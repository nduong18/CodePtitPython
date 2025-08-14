import math
t = int(input())
for _ in range(t):
    n = input()
    r = list(map(int,input().split()))
    r.sort(key=lambda x: (math.prod([int(i) for i in str(x)]), x))
    print(*r)