t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    i = 1
    while True:
        r = ""
        x = i
        while x != 0:
            r += str(x % 3)
            x //= 3
        r = r[::-1]
        if r.count("2") > len(r) / 2:
            print(r, end=" ")
            cnt += 1
        i += 1
        if cnt == n: break
    print()