import math
n, k = map(int, input().split())
z2 = 10**k
z1 = 10**(k-1)
r = []
cnt = 0
for i in range(z1,z2):
    if (math.gcd(n,i) == 1):
        print(i, end=" ")
        cnt += 1
        if cnt % 10 == 0:
            print()