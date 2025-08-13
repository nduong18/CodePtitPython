t = int(input())
for _ in range(t):
    x = input()
    p = [x[i:i+2] for i in range(0,len(x),2)]
    r = ""
    for s in p:
        r += s[0]*(int(s[1]))
    print(r)