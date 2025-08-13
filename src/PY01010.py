t = int(input())
for _ in range(t):
    x = input()
    a = int(x[:2])
    b = int(x[-2:])
    if (a == b):
        print("YES")
    else:
        print("NO")