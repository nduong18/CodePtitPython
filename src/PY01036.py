t = int(input())
for _ in range(t):
    n = int(input())
    s = 2 if n % 2 == 0 else 1
    r = 0
    for i in range(s,n+1,2):
        r += float(1) / i
    print(f"{r:.6f}")