t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    r.sort(key = lambda x: (sum(int(i) for i in str(x)), x))
    print(*r)
        