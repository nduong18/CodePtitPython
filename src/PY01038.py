t = int(input())
for _ in range(t):
    x = int(input())
    if x % 7 == 0:
        print(x)
        continue
    check = False
    for _ in range(1000):
        res = int(str(x)[::-1])
        x += res
        if x % 7 == 0:
            print(x)
            check = True
            break
    if not check: print("-1")
