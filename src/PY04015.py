class HoaDon:
    def __init__(self, ten, so, stt):
        self.ten = ten
        self.stt = f"KH{stt:02d}"      
        donGia = 0
        phuPhi = 00
        if so <= 50:
            self.tongTien = 100 * so + (100 * so) * 2 / 100
        elif so <= 100:
            res = 50 * 100 + (so - 50) * 150
            self.tongTien = res + res * 3 / 100
        else:
            res = 50 * 100 + 50 * 150 + (so - 100) * 200
            self.tongTien = res + res * 5 / 100       

    def show(self):
        print(f"{self.stt} {self.ten} {int(round(self.tongTien))}")

t = int(input())
ds = list()
for i in range(t):
    ten = input()
    x = int(input())
    y = int(input())
    HD = HoaDon(ten, y - x, i + 1)
    ds.append(HD)

ds.sort(key=lambda x: -x.tongTien)
for i in ds:
    i.show()