from datetime import *
class Phim:
    def __init__(self, stt, tl, kc, ten, tap):
        self.stt = f"P{stt:03d}"
        self.tl = theLoai[int(tl[2:]) - 1]
        self.kc = kc
        self.date = datetime.strptime(kc, "%d/%m/%Y")
        self.ten = ten
        self.tap = tap
    
    def show(self):
        print(self.stt, self.tl, self.kc, self.ten, self.tap)



theLoai = list()
ds = list()
n, m = map(int, input().split())
for _ in range(n):
    s = input()
    theLoai.append(s)

for i in range(m):
    ds.append(Phim(i+1, input(), input(), input(), int(input())))

ds.sort(key=lambda x: (x.date, x.ten, -x.tap))
for i in ds: i.show()
