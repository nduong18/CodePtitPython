import math
a,k,n = map(int,input().split())

# Công thức modulo
mod = (k - (a%k)) % k
b = mod if mod != 0 else k

r = []
while a+b <= n:
    x = a+b
    if x % k == 0:
        r.append(str(b))
    b += k

if len(r) == 0:
    print("-1")
else:
    print(" ".join(r))