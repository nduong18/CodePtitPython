import math

def is_prime(x):
    if x < 2: 
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False              
    return True

def gcd(a,b):
    return math.gcd(a,b)

t = int(input())
for _ in range(t): 
    n = int(input())
    k = 0
    for i in range(1,n):
        if (gcd(i,n) == 1):
            k += 1
    if (is_prime(k)):
        print("YES")
    else:
        print("NO")