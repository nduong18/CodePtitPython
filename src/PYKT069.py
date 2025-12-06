from datetime import *
class CaThi:
    def __init__(self, ma, ngay, gio, id):
        self.ma = f"C{ma:03d}"
        self.NGAY = ngay
        self.GIO = gio
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.gio = timedelta(int(gio[:2]), int(gio[3:]))
        self.id = id
    def show(self):
        print(self.ma, self.NGAY, self.GIO, self.id)

ds = []
filename = r"CATHI.in"
with open(filename, "r") as f:
    t = int(f.readline().strip())
    for i in range(t):
        ngay = f.readline().strip()
        gio = f.readline().strip()
        id = f.readline().strip()
        ds.append(CaThi(i+1, ngay, gio, int(id)))
ds.sort(key=lambda x: (x.ngay, x.gio, x.ma))
for i in ds: i.show()