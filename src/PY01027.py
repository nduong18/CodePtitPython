s = input()

if not s or any(c not in '68' for c in s):
    print('NO')
    exit()

if ((s[:1] == '6' or s[:2] == '68' or s[:3] == '688')):
    print('YES')
else:
    print('NO')