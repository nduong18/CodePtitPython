t = int(input())
for _ in range(t):
    s1 = input()
    s2 = s1[::-1]
    n = len(s1)
    check = True
    for i in range(1,n):
        a = abs(ord(s1[i])-ord(s1[i-1]))
        b = abs(ord(s2[i])-ord(s2[i-1]))
        if a != b:
            check = False
            break

    if (check): print("YES")        
    else: print("NO")