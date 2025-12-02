data = {
    "A" : 100, "B" : 500, "C" : 200
}

class KH:
    def __init__(self, ma, ten, a, b, c, d):
        self.ma = ma
        self.ten = ten
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def show(self):
        print(self.ma, self.ten, self.a, self.b, self.c, self.d)

ds = list()
t = int(input())
for i in range(t):
    ten = input().lower().split()
    TEN = " ".join(i.title() for i in ten)
    s = input().split()
    loai = s[0]
    diff = int(s[2]) - int(s[1])
    if diff < data[loai]:
        ttdm = diff * 450
    else:
        ttdm = data[loai] * 450
    
    if diff > data[loai]:
        tvdm = (diff - data[loai]) * 1000
    else:
        tvdm = 0   
    VAT = tvdm // 20
    tong = ttdm + tvdm + VAT
    ds.append(KH(f"KH{i+1:02}", TEN, ttdm, tvdm, VAT, tong))
ds.sort(key=lambda x: -x.d)
for i in ds: i.show()