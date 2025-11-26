import math

def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while (True):
    x = input()
    if (x == '-1'):
        break
    l,r = map(int, x.split())
    n = int(input())
    cnt = 0
    a = []
    for i in range(l,r+1):
        if check(i):
            a.append(i)
    print(a)