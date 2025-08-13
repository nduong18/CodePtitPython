import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    x = input()
    if (is_prime(sum(int(i) for i in x))):
        print("YES")
    else:
        print("NO")
