import math

def is_prime(y):
    if y < 2:
        return False
    else:
        for z in range(2,(int)(math.sqrt(y)+1)):
            if y % z == 0:
                return False
    return True

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    x = math.gcd(a,b)
    x = str(x)
    sum = 0
    for i in x:
        sum += int(i)
    if (is_prime(sum)):
        print("YES")
    else:
        print("NO")

