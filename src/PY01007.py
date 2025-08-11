t = int(input())
for _ in range(t):
    a,b,c = map(float,input().split())
    y = 0
    s = a
    while s < c:
        s += (s * (b/100))
        y += 1
    print(y)
