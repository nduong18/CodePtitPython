class ThiSinh:
    def __init__(self, stt, ten, team, truong):
        self.stt = stt
        self.ten = ten
        self.team = team
        self.truong = truong
    def show(self):
        print(self.stt, self.ten, self.team, self.truong)

ds1 = list()
ds2 = list()
n = int(input())
for _ in range(n):
    a = input()
    b = input()
    c = {a:b}
    ds1.append(c)
m = int(input())
for i in range(m):
    ten = input()
    team = int(input()[4:])
    team_dict = ds1[team-1]
    team_code = list(team_dict.keys())[0]
    truong = team_dict[team_code]
    ds2.append(ThiSinh(f"C{i+1:03d}", ten, team_code, truong))
ds2.sort(key=lambda x: x.ten)
for i in ds2: i.show()

