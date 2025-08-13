t = int(input())
for _ in range(t):
    x = input()
    num = ""
    res = []
    for c in x:
        if c.isdigit():
            num += c
        else:
            if num:
                res.append(num)
                num = ""
    if num:
        res.append(num)

    print(max(int(i) for i in res))