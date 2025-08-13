def rut_gon(x):
    seen = set(x)
    res = []
    for c in seen:
        if c not in res:
            res.append(c)
        seen.add(c)
    return "".join(res)

t = int(input())
for _ in range(t):
    x = input().strip()
    print(rut_gon(x))
    