import math
class PhanSo:
    def __init__(self, tu, mau):
        x = math.gcd(tu, mau)
        self.tu = tu / x 
        self.mau = mau / x
    def show(self):
        print(f"{int(self.tu)}/{int(self.mau)}")

x,y = map(int, input().split())
p = PhanSo(x, y)
p.show()