t = int(input())
for _ in range(t):
    x = input()
    res = ""
    cnt = 1
    for i in range(1,len(x)):
        if x[i] != x[i-1]:
            res += f"{cnt}{x[i-1]}"
            cnt = 1
        else:
            cnt += 1
    res += f"{cnt}{x[-1]}"
    print(res)