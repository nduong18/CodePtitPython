data = "47"
t = int(input())
for _ in range(t):
    x = input()
    v = all([i in data for i in x])
    if v: print("YES")
    else: print("NO")