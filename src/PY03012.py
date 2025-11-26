class SinhVien:
    def __init__(self, ten, x, y):
        self.ten = ten
        self.x = x
        self.y = y

a = []
t = int(input())
for _ in range(t):
    ten = input()
    x, y = map(int, input().split())
    sv = SinhVien(ten, x, y)
    a.append(sv)

a.sort(key=lambda hs: (-hs.x , hs.y, hs.ten))
for sv in a:
    print(f"{sv.ten} {sv.x} {sv.y}")