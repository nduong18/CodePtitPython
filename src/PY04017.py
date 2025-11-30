class VanToc:
    def __init__(self, ten, tp, vt):
        self.ten = ten
        self.tp = tp
        res = ""
        for i in tp.split():
            res += i[0]
        for i in ten.split():
            res += i[0]
        self.ma = res
        self.vt = vt
    def show(self):
        print(self.ma, self.ten, self.tp, round(self.vt), "Km/h")
        
t = int(input())
ds = list()
for _ in range(t):
    ten = input().strip()
    tp = input().strip()
    tg = input().strip().split(":")
    TG = (int(tg[0]) * 60 + int(tg[1]) - 360) / 60
    vt = 120 / TG 
    VT = VanToc(ten, tp, vt)
    ds.append(VT)

ds.sort(key=lambda x: -x.vt)
for i in ds: i.show()