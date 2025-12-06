def tn(x):
    z = str(x)
    if len(z) < 2:
        return False
    return z == z[::-1]

res = {}
maxR = -10**18
n,m = map(int, input().split())
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        z = a[j]
        if tn(z):
            if z not in res:
                res[z] = []
            res[z].append(f"Vi tri [{i}][{j}]")
            if z > maxR:
                maxR = z
if maxR == -10**18:
    print("NOT FOUND")
else:
    print(maxR)
    print("\n".join(res[maxR]))