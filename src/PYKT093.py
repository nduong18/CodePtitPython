from decimal import *
class SinhVien:
    def __init__(self, stt, ten, diem, rank):
        self.stt = f"SV{stt:02d}"
        self.ten = ten
        self.diem = diem
        self.rank = rank
    def show(self):
        print(self.stt, self.ten, Decimal(self.diem).quantize(Decimal('0.01'), ROUND_HALF_UP), self.rank)
ds = list()
t = int(input())
for i in range(t):
    ten = " ".join([i.title() for i in  input().lower().split()])
    d = (3 * Decimal(input()) + 3 * Decimal(input()) + 2 * Decimal(input())) / 8
    ds.append(SinhVien(i+1, ten, d, 0))
ds.sort(key=lambda x: -x.diem)
ds[0].rank = 1
for i in range(1, len(ds)):
    if ds[i].diem == ds[i-1].diem:
        ds[i].rank = ds[i-1].rank
    else:
        ds[i].rank = i+1
for i in ds: i.show()

    
