import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    x = input()
    check = True
    for i in range(len(x)):
        if i % 2 == 0 and int(x[i]) % 2 != 0:
            check = False
            break
        elif i % 2 != 0 and int(x[i]) % 2 == 0:
            check = False
            break
    
    if (check and is_prime(sum((int(i) for i in x)))): print("YES")
    else: print("NO")
