from datetime import *
class LichThi:
    def __init__(self, stt, ma, ngay, gio, nhom):
        self.stt = f"T{stt:03d}"
        self.ma = ma
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom
        self.date = datetime.strptime(ngay, "%d/%m/%Y")
        self.time = timedelta(hours=int(gio[:2]), minutes=int(gio[3:]))
        self.MA = int(ma[3:])
    def show(self):
        print(self.stt, self.ma, DIC[self.ma], self.ngay, self.gio, self.nhom)

DIC = {}
ds = list()
n,m = map(int, input().split())
for _ in range(n):
    x = input()
    y = input()
    DIC[x] = y
for i in range(m):
    s = input().split()
    ds.append(LichThi(i+1, s[0], s[1], s[2], s[3]))
ds.sort(key=lambda x: (x.date, x.time, x.MA))
for i in ds: i.show()