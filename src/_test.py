import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def ps(self):
        x = math.gcd(self.tu, self.mau)
        return f"{int(self.tu / x)}/{int(self.mau / x)}"

tu, mau = map(int, input().split())
p = PhanSo(tu, mau)
print(p.ps())