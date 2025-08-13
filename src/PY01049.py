import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    x = input()
    z1 = z2 = 0
    for i in x:
        if i in '2357':
            z1 += 1
        else:
            z2 += 1
    if (is_prime(len(x)) and z1 > z2):
        print("YES")
    else:
        print("NO")
