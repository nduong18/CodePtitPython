import math
def is_prime(x):
    if x < 2: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

maxR = -10**18
res = {}
n, m = map(int, input().split())
for i in range(n):
    x = list(input().split())
    for j in range(m):
        z = int(x[j])
        if is_prime(z):
            if z not in res:
                res[z] = []
            res[z].append(f"Vi tri [{i}][{j}]")
            if z > maxR: maxR = z
            
if maxR == -10**18: print("NOT FOUND")
else:
    print(maxR)
    for i in res[maxR]: print(i)