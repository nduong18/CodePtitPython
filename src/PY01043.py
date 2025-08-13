t = int(input())
for _ in range(t):
    x = int(input())
    for i in range(22,x):
        i = str(i)
        i1 = i == i[::-1]
        i2 = all(c in '02468' for c in i)
        i3 = len(i) % 2 == 0
        if i1 and i2 and i3:
            print(i, end=" ")
    print()