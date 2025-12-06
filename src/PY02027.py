t = int(input())
res = []
for _ in range(t):
    s = input()
    x = "".join(i if i.isdigit() else " " for i in s)
    X = list(map(int, x.split()))
    for i in X: res.append(i)
res = sorted(res, reverse=False)
for i in res: print(i)
    