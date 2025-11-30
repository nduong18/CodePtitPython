class HoaDon:
    def __init__(self, stt, ten, sl, dg, ck):
        self.stt = stt
        self.ten = ten
        self.sl = sl
        self.dg = dg
        self.ck = ck
        self.tongTien = dg * sl - ck
    def show(self):
        print(self.stt, self.ten, self.sl, self.dg, self.ck, self.tongTien)

t = int(input())
ds = list()
for i in range(t):
    ds.append(HoaDon(input(), input(), int(input()), int(input()), int(input())))
ds.sort(key=lambda x: -x.tongTien)
for i in ds: i.show()
