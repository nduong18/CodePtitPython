import math
t = int(input())
for _ in range(t):
    x = input()
    i1 = sum(int(x[i]) for i in range(0,len(x),2))
    check = all(x[i] == '0' for i in range(1,len(x),2))
    i2 = 1
    if check:
        i2 = 0
    else:
        i2 = math.prod(int(x[i]) for i in range(1,len(x),2) if x[i] != '0')
    print(i1,i2)
