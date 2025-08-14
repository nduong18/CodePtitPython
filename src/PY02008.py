import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

def first_n_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n,x = map(int,input().split())
z = first_n_prime(n)
r = [x]
for i in z:
    r.append(r[-1]+i)

print(*r)