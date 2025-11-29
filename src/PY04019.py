class NhanVien:
    def __init__(self, ten, lt, th, stt):
        self.ten = ten
        self.stt = f"TS0{stt:01d}"

        if lt > 10: lt /= 10
        if th > 10: th /= 10
        self.diemTB = (lt + th) / 2

        if self.diemTB < 5:
            self.trangThai = "TRUOT"
        elif self.diemTB < 8:
            self.trangThai = "CAN NHAC"
        elif self.diemTB < 9.5:
            self.trangThai = "DAT"
        else:
            self.trangThai = "XUAT SAC"

    def show(self):
        print(f"{self.stt} {self.ten} {self.diemTB:.2f} {self.trangThai}")

t = int(input())
ds = list()
for i in range(t):
    ten = input()
    x = float(input())
    y = float(input())
    NV = NhanVien(ten, x, y, i + 1)
    ds.append(NV)

ds.sort(key=lambda x: -x.diemTB)
for i in ds:
    i.show()
