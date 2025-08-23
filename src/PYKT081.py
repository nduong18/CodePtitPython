t = int(input())
for _ in range(t):
    x = input().strip()
    r = x.split(".")
    if len(r) == 4 and all(i.isdigit() and int(i) >= 0 and int(i) <= 255 for i in r):
        print("YES")
    else:
        print("NO")        