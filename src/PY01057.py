import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    x = input()
    check = True
    for i in range(len(x)):
        if x[i] in '2357' and not is_prime(i):
            check = False
            break
    if (check): print("YES")
    else: print("NO")
    