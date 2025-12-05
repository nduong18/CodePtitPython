t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    r = "A"
    x = "B"
    for _ in range(n-1):
        r = r + x + r
        x = chr(ord(x)+1)
    print(r[k-1])

