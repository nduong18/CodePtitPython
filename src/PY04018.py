class GiaoVien:
    def __init__(self, stt, ten, mon, tin, cm):
        self.stt = f"GV{stt:02d}"
        self.ten = ten
        
        if mon[0] == 'A':
            self.mon = "TOAN"
        elif mon[0] == 'B':
            self.mon = "LY"
        elif mon[0] == 'C':
            self.mon = "HOA"

        if mon[1] == '1':
            self.uuTien = 2
        elif mon[1] == '2':
            self.uuTien = 1.5
        elif mon[1] == '3':
            self.uuTien = 1
        elif mon[1] == '4':
            self.uuTien = 0

        self.tongDiem = tin * 2 + cm + self.uuTien
        if (self.tongDiem >= 18):
            self.tt = "TRUNG TUYEN"
        else:
            self.tt = "LOAI"

    def show(self):
        print(self.stt, self.ten, self.mon, f"{self.tongDiem:.1f}", self.tt)

t = int(input())
ds = list()
for i in range(t):
    ds.append(GiaoVien(i + 1, input().strip(), input().strip(), float(input()), float(input())))
ds.sort(key=lambda x: -x.tongDiem)
for i in ds: i.show()