t = int(input())
for _ in range(t):
    s = input()
    S = []
    D = []
    for i in range(len(s)):
        if s[i].isalpha():
            S.append(s[i])
        else:
            D.append(s[i])
    S.sort()
    sumD = sum(int(i) for i in D)
    print(''.join(S) + str(sumD))