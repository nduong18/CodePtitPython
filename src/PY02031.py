import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

a,b = map(int,input().split())
r = []
for _ in range(a):
    z = list(map(int,input().split()))
    r.append(z)

for i in r:
    for j in i:
        if is_prime(j):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()