import math
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = sorted([x for x in a if is_prime(x)])
idx = 0
for i in a:
    if i in b:
        print(b[idx], end=" ")
        idx += 1
    else:
        print(i, end=" ")
