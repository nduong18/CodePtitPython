ten = input()
ns = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())

NS = ns.split('/')
nS = ''
for i in range(2):
    if len(NS[i]) < 2:
        nS += '0' + NS[i] + '/'
    else:
        nS += NS[i] + '/'
nS += NS[2]

print(f"{ten} {nS} {diem1+diem2+diem3:.1f}")