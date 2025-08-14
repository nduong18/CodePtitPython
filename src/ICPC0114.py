import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    x = input()
    i1 = is_prime(int(x))
    i2 = is_prime(int(x[::-1]))
    i3 = is_prime(sum(int(i) for i in x))
    i4 = all(is_prime(int(i)) for i in x)
    if i1 and i2 and i3 and i4:
        print("Yes")
    else:
        print("No")