t = int(input())
for _ in range(t):
    x = input()
    sum_digit = sum([int(i) for i in x])
    check = all(abs(ord(a)-ord(b)) == 2 for a,b in zip(x,x[1:]))
    if (sum_digit % 10 == 0 and check): print("YES")
    else: print("NO")