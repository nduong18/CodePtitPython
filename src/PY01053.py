t = int(input())
for _ in range(t):
    x = input()
    r = sum(map(int,str(x)))
    if r % 3 == 0: print("YES")
    else: print("NO")