class DS1:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop

class DS2:
    def __init__(self, ma, diem):
        self.ma = ma
        self.diem = diem

t = int(input())
ds1 = list()
ds2 = list()
for _ in range(t):
    ma = input()
    ten = input()
    lop = input()
    ds1.append(DS1(ma, ten, lop))

for _ in range(t):
    s = input().split()
    ma = s[0]
    cc = s[1]
    diem = 10
    for i in cc:
        if i == 'v':
            diem -= 2
        elif i == 'm':
            diem -= 1
    
    if diem <= 0: diem = 0
    ds2.append(DS2(ma, diem))

for i in ds1:
    for j in ds2:
        if i.ma == j.ma:
            if j.diem == 0:
                print(i.ma, i.ten, i.lop, j.diem, "KDDK")
            else:
                print(i.ma, i.ten, i.lop, j.diem)
                
