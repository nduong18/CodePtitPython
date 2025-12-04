s = input().strip()
while len(s) != 1:
    x = len(s) // 2
    s = str(int(s[:x]) + int(s[x:]))
    print(s)