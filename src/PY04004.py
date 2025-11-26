import math
class PhanSo:
    def __init__(self, tu, mau):
        x = math.gcd(tu, mau)
        self.tu = int(tu / x) 
        self.mau = int(mau / x)
    def add(self, p):
        x = self.tu * p.mau + self.mau * p.tu
        y = self.mau * p.mau
        return PhanSo(x, y)
    def show(self):
        print(f"{self.tu}/{self.mau}")

tu1, mau1, tu2, mau2 = map(int, input().split())
p1 = PhanSo(tu1, mau1)
p2 = PhanSo(tu2, mau2)
p3 = p1.add(p2)
p3.show()
