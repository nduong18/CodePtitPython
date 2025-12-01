data = {
    "A" : {"1-3":10, "4-8":12, "9-15":14, ">=16":20},
    "B" : {"1-3":10, "4-8":11, "9-15":13, ">=16":16},
    "C" : {"1-3":9, "4-8":10, "9-15":12, ">=16":14},
    "D" : {"1-3":8, "4-8":9, "9-15":11, ">=16":13}
}
def get_value(nhom, nam):
    if 1 <= nam <= 3:
        key = "1-3"
    elif 4 <= nam <= 8:
        key = "4-8"
    elif 9 <= nam <= 15:
        key = "9-15"
    else:
        key = ">=16"
    return data[nhom][key]
DIC = {}
n = int(input())
for _ in range(n):
    s = input()
    a = s[:2]
    b = s[3:]
    DIC[a] = b
m = int(input())
for _ in range(m):
    ma = input()
    ten = input()
    lcb = int(input())
    snc = int(input())
    nhom = ma[0]
    nam = int(ma[1:3])
    pb = ma[3:]  
    luong = lcb * snc * get_value(nhom,nam) * 1000
    print(ma, ten, DIC[pb], luong)
