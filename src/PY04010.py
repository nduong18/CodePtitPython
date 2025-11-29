ten = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())

diem = d1 + d2 + d3

NS = ns.split('/')
res = ""
for i in NS:
    if len(i) < 2:
        res += "0" + i + "/"
    elif len(i) == 4:
        res += i
    else:
        res += i + "/"
print(f"{ten} {res} {diem:.1f}")
