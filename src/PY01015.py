t = int(input())
for _ in range(t):
    x = input()
    check = False
    for i in range(0,len(x)-1):
        a = int(x[i])
        b = int(x[i+1])
        if (a > b):
            check = True
            break
    
    if (check):
        print("NO")
    else:
        print("YES")