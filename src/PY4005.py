import math

def dis(x1, y1, x2, y2):
    return math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))

t = int(input())

for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    a = dis(x1, y1, x2, y2)
    b = dis(x1, y1, x3, y3)
    c = dis(x2, y2, x3, y3)

    if max([a,b,c])*2 >= a+b+c: print('INVALID')
    else: print(f'{round(a+b+c,3):.3f}')