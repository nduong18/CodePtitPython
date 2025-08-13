import math

t = int(input())
for _ in range(t):
    x = input()
    i1 = len(x) % 2 != 0
    i2 = x[0] != x[1]
    i3 = x[0] == x[len(x)-1] and all(x[i] == x[0] for i in range(0,len(x),2))
    if i1 and i2 and i3:
        print("YES")
    else:
        print("NO")