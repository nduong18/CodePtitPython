import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    x = input()
    i1 = is_prime(len(x))
    p1 = p2 = 0
    for i in x:
        if is_prime(int(i)):
            p1 += 1
        else:
            p2 += 1
    i2 = p1 > p2
    if i1 and i2:
        print("YES")
    else:
        print("NO")