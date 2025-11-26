import re
a = {}
t = int(input())
for _ in range(t):
    s = re.split("[^a-z0-9]", input().lower().strip())
    for i in s:
        if i != '':
            if a.get(i) is None: a[i] = 1
            else: a[i] += 1

ans = sorted(a, key=lambda x: (-a[x], x))
for i in ans: print(i, a[i])

