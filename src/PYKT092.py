class TuyenSinh:
    def __init__(self, stt, ten, diem, tt):
        self.stt = f"TS{stt:02d}"
        self.ten = ten
        self.diem = diem
        self.tt = tt
    def show(self):
        print(self.stt, self.ten, self.diem, self.tt)
ds = list()
t = int(input())
for i in range(t):
    ten = input().lower().split()
    diem = float(input())
    dt = input()
    kv = int(input())
    TEN = " ".join([i.title() for i in ten])
    if kv == 1:
        diem += 1.5
    elif kv == 2:
        diem += 1   
    if dt != "Kinh":
        diem += 1.5
    if diem < 20.5:
        tt = "Truot"
    else:
        tt = "Do"
    ds.append(TuyenSinh(i + 1, TEN, diem, tt))
ds.sort(key=lambda x: (-x.diem, x.stt))
for i in ds: i.show()