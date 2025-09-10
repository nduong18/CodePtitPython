import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def toiGian(self):
        tmp = math.gcd(self.tu, self.mau)
        self.tu /= tmp
        self.mau /= tmp
    def showInfo(self):
        self.toiGian()
        print(f"{int(self.tu)}/{int(self.mau)}")

a,b = map(int, input().split())
p = PhanSo(a, b)
p.showInfo()

        