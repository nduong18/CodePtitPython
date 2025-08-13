t = int(input())
for _ in range(t):
    x = input()
    y = x[::-1]
    check = True
    for i in range(1,len(x)):
        if abs(ord(x[i]) - ord(x[i-1])) != abs(ord(y[i]) - ord(y[i-1])):
            check = False
            break
    if check: print("YES")
    else: print("NO")