def is_valid(x):
    for i in x:
        if int(i) % 2 == 1:
            return False
    return True

t = int(input())
res = []

num = 2
while num <= 888:
    if (is_valid(str(num))):
        tmp = str(num)
        res.append(int(tmp + tmp[::-1]))
    num += 2

for _ in range(t):
    n = int(input())
    for c in res:
        if (c >= n):
            break
        print(c, end = ' ')
    print()
