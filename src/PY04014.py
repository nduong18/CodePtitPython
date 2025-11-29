from decimal import ROUND_HALF_UP, Decimal
class HocSinh:
    def __init__(self, tt, ten, diemtb):
        self.tt = tt
        self.ten = ten
        self.diemtb = Decimal(diemtb).quantize(Decimal('0.1'), ROUND_HALF_UP)
        
        if diemtb >= 9:
            self.hocluc = 'XUAT SAC'
        elif diemtb >= 8:
            self.hocluc = 'GIOI'
        elif diemtb >= 7:
            self.hocluc = 'KHA'
        elif diemtb >= 5:
            self.hocluc = 'TB'
        else:
            self.hocluc = 'YEU'

    def show(self):
        print(f"{self.tt} {self.ten} {self.diemtb} {self.hocluc}")

t = int(input())
a = []
for i in range(t):
    ten = input().strip()
    d1,d2,d3,d4,d5,d6,d7,d8,d9,d10 = map(Decimal, input().split())
    diemtb = (d1*2 + d2*2 + d3 +d4 +d5 + d6 + d7 + d8 + d9 + d10) / Decimal(12)
    tt = f"HS{i+1:02d}"
    hs = HocSinh(tt, ten, diemtb)
    a.append(hs)

a.sort(key=lambda hs: (-hs.diemtb, hs.tt))

for hs in a:
    hs.show()