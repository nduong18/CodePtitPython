class LuongMua:
    def __init__(self, ten, tg, lm, stt):
        self.ten = ten
        self.tg = tg
        self.lm = lm
        self.stt = f"T{stt:02d}"

t = int(input())
ds = list()
for i in range(t):
    ten = input()
    bd = input()
    kt = input()
    lm = float(input())
    BD = bd.split(":")
    KT = kt.split(":")
    x = int(BD[0]) + int(BD[1]) / 60
    y = int(KT[0]) + int(KT[1]) / 60  
    L = LuongMua(ten, y - x, lm, i+1)
    
    found = False
    for obj in ds:
        if obj.ten == L.ten:
            obj.tg += L.tg
            obj.lm += L.lm
            found = True
            break
    
    if not found: 
        ds.append(L)

for i in ds:
    print(i.stt, i.ten, f"{i.lm / i.tg :.2f}")
    
