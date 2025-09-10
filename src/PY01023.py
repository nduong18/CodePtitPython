import math
t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for i in range(2,(int(math.sqrt(n)) + 1)):
        while n % i == 0:
            dic[i] = dic.get(i,0) + 1
            n /= i
    if n > 1:
        dic[n] = dic.get(n,0) + 1

    for key in sorted(dic.keys()):
        print(key,dic[key])
    print()

