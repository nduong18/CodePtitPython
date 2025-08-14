import math

t = int(input())
for _ in range(t):
    x = input()
    i1 = int(x) == sum(math.factorial(int(i)) for i in x)
    if i1: print("Yes")
    else: print("No")
        