t = int(input())
for _ in range(t):
    x = input()
    if set(x) - {'4','7'}:
        print("NO")
    else:
        print("YES")