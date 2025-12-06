from datetime import *

# ------------------ CLASS ------------------
class MonThi:
    def __init__(self, ma, ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc

class CaThi:
    def __init__(self, stt, ngay, gio, phong):
        self.ma = f"C{stt:03d}"
        self.ngay_str = ngay
        self.gio_str = gio
        self.phong = phong

        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        h, m = map(int, gio.split(":"))
        self.time = timedelta(hours=h, minutes=m)

class LichThi:
    def __init__(self, cat, mon, nhom, sv):
        self.cat = cat
        self.mon = mon
        self.nhom = nhom
        self.sv = sv

# ------------------ READ FILE ------------------
fileMon = r"MONTHI.in"
fileCa = r"CATHI.in"
fileLich = r"LICHTHI.in"

# đọc môn thi
dsMon = {}
with open(fileMon) as f:
    t = int(f.readline().strip())
    for _ in range(t):
        ma = f.readline().strip()
        ten = f.readline().strip()
        hinh = f.readline().strip()
        dsMon[ma] = MonThi(ma, ten, hinh)

# đọc ca thi
dsCa = {}
with open(fileCa) as f:
    t = int(f.readline().strip())
    for i in range(1, t+1):
        ngay = f.readline().strip()
        gio = f.readline().strip()
        phong = f.readline().strip()
        ca = CaThi(i, ngay, gio, phong)
        dsCa[ca.ma] = ca

# đọc lịch thi
dsLich = []
with open(fileLich) as f:
    t = int(f.readline().strip())
    for _ in range(t):
        maCa, maMon, nhom, sv = f.readline().strip().split()
        dsLich.append(LichThi(maCa, maMon, nhom, sv))

# ------------------ SORT ------------------
dsLich.sort(key=lambda x: (
    dsCa[x.cat].ngay,
    dsCa[x.cat].time,
    x.cat
))

# ------------------ OUTPUT ------------------
for lt in dsLich:
    ca = dsCa[lt.cat]
    mon = dsMon[lt.mon]

    print(
        ca.ngay_str,
        ca.gio_str,
        ca.phong,
        mon.ten,
        lt.nhom,
        lt.sv
    )
