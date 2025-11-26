x = str(abs(int(input())))
cnt = 0
if len(x) == 1:
    print(1)
else:
    while len(x) > 1:
        x = str(sum((ord(i) - ord('0')) for i in x))
        cnt += 1
    print(cnt)