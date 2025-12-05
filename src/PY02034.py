s = input()
a = []
for i in range(0, len(s) - 1, 2):
    a.append(int(s[i:i+2]))

seen = set()
res = []
cnt = {}

for x in a:
    if x not in seen:
        seen.add(x)
        res.append(x)
    cnt[x] = cnt.get(x, 0) + 1
for i in res:
    print(i, cnt[i])