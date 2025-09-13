t = int(input())
for _ in range(t):
    x = input()
    setX = set([i for i in x])
    a = True
    for i in range(0,len(x)-2):
        if x[i] != x[i+2]:
            a = False
            break
    if (a and len(setX)):
        print("YES")
    else:
        print("NO")
