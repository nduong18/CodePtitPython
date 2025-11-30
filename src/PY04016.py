from datetime import *

class HoaDon:
    def __init__(self, stt, ten, sp, ngay, dv):
        self.stt = f"KH{stt:02d}"
        self.ten = ten
        self.sp = sp
        self.ngay = ngay

        tang = int(sp[0])
        gia = 0
        if tang == 1:
            gia = 25
        elif tang == 2:
            gia = 34
        elif tang == 3:
            gia = 50
        elif tang == 4:
            gia = 80
        
        self.thanhTien = gia * ngay + dv
    
    def show(self):
        print(self.stt, self.ten, self.sp, self.ngay, self.thanhTien)
    
t = int(input())
ds = list()
for i in range(t):
    ten = input().strip()
    sp = input().strip()
    vao = input().strip()
    ra = input().strip()
    dv = int(input())
    VAO = datetime.strptime(vao, "%d/%m/%Y")
    RA = datetime.strptime(ra, "%d/%m/%Y")
    diff = RA - VAO
    HD = HoaDon(i+1, ten, sp, diff.days + 1, dv)
    ds.append(HD)

ds.sort(key=lambda x: -x.thanhTien)
for i in ds: i.show()