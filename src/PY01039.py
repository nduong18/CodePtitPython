t = int(input())
for _ in range(t):
    x = input().strip()
    i1 = len(set(x)) == 2
    i2 = all(x[i] == x[i+2] for i in range(len(x)-2))
    if (i1 and i2): print("YES")
    else: print("NO")