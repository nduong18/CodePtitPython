import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    x = input()    
    for i in range(int(x)):
        i1 = is_prime(i)
        i2 = str(i) != str(i)[::-1] and is_prime(int(str(i)[::-1]))
        if i1 and i2: 
            print(i, end=" ")
    print()
