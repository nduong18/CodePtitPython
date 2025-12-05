s = input()
a = []
for i in range(0, len(s)-1, 2):
    z = s[i:i+2]
    if len(z) == 2: a.append(int(z))
a = list(sorted(set(a)))
for i in a: print(i, end=" ")