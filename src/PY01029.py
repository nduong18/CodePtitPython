import math
t = int(input())
for _ in range(t):
    x = input()
    z = x[::-1]
    if (math.gcd(int(x),int(z)) == 1): print("YES")
    else: print("NO")