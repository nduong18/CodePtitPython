import math
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
a = list(map(int,input().split()))
b = list(set(a))
B = []
for i in a:
    if i in b:
        B.append(i)
        b.remove(i)
check = False
for i in range(len(B)):
    sum1 = sum(B[i] for i in range(0, i+1))
    sum2 = sum(B[i] for i in range(i+1, len(B)))
    if (is_prime(sum1) and is_prime(sum2)):
        print(i)
        check = True
        break
if not check: print("NOT FOUND")