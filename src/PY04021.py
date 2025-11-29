class Game:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        VAO = vao.split(':')
        RA = ra.split(':')
        self.GIO = (int(RA[0]) * 60 + int(RA[1]) - int(VAO[0]) * 60 - int(VAO[1]))
        self.tg = f"{self.GIO // 60} gio {self.GIO % 60} phut"

    def show(self):
        print(self.ma, self.ten, self.tg)

t = int(input())
ds = list()
for _ in range(t):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    ds.append(Game(ma, ten, vao, ra))

ds.sort(key=lambda x: -x.GIO)
for i in ds: i.show()
