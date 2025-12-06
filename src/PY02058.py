minR = 10**18
maxR = -10**18
v = []
res = {}
n, m = map(int, input().split())
for i in range(n):
    x = list(input().split())
    v.append(x)
    for j in range(m):
        z = int(x[j])
        if z < minR: minR = z
        if z > maxR: maxR = z

check = False
num = maxR - minR
for i in range(n):
    z = v[i]
    for j in range(m):
        if int(z[j]) == num:
            check = True
            if num not in res:
                res[num] = []
            res[num].append(f"Vi tri [{i}][{j}]")
if check:    
    print(num)
    for i in res[num]: print(i)
else: print("NOT FOUND")