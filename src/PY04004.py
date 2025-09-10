import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def toiGian(self):
        tmp = math.gcd(self.tu, self.mau)
        self.tu //= tmp
        self.mau //= tmp
    def cong(self, p):
        tuMoi = self.tu * p.mau + p.tu * self.mau
        mauMoi = self.mau * p.mau
        self.tu, self.mau = tuMoi, mauMoi
        self.toiGian()
    def showInfo(self):
        print(f"{self.tu}/{self.mau}")

a,b,c,d = map(int, input().split())
p1 = PhanSo(a,b)
p2 = PhanSo(c,d)
p1.cong(p2)
p1.showInfo()