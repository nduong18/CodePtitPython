t = int(input())
for _ in range(t):
    x = input()
    n = input()
    len_n = len(n)
    cnt = 0
    for i in range(0,len(x),len_n):
        if x[i:i+len_n] == n:
            print(x[i:i+len_n],i, end=",")
    print()
