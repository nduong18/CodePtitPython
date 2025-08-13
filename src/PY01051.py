t = int(input())
for _ in range(t):
    x = input()
    z = str(sum(map(int,x)))
    if z == z[::-1] and len(z) > 1:
        print("YES")
    else:
        print("NO")