import math
t = int(input())
for _ in range(t):
    x = input()
    i1 = math.prod(int(x[i]) for i in range(0,len(x),2) if x[i] != '0')
    i2 = sum(int(x[i]) for i in range(1,len(x),2))
    print(i1,i2)