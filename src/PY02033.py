s = input()
a = []
for i in range(0, len(s) - 1, 2):
    a.append(s[i:i+2])

seen = set()
res = []

for x in a:
    if x not in seen:
        seen.add(x)
        res.append(x)
print(*res)