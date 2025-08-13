t = int(input())
for _ in range(t):
    x = input()
    r = 1
    for i in x:
        if int(i) != 0:
            r *= int(i)
    print(r)