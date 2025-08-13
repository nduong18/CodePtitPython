t = int(input())
for _ in range(t):
    b = int(input())
    x = input()
    r = int(x,b)
    

    if b == 2:
        kq = bin(r)[2:]
    elif b == 8:
        kq = oct(r)[2:]
    elif b == 16:
        kq = hex(r)[2:].upper()

    print(kq)