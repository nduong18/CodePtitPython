class SoPhuc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):
        a = self.x
        b = self.y
        c = p.x
        d = p.y
        return SoPhuc(a+c,b+d)
    
    def mul(self, p):
        a = self.x
        b = self.y
        c = p.x
        d = p.y
        return SoPhuc(a*c - b*d, a*d + b*c)

t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    p1 = SoPhuc(a,b)
    p2 = SoPhuc(c,d)
    ADD = p1.add(p2)
    C = ADD.mul(p1)
    D = ADD.mul(ADD)
    print(f"{C.x} + {D.y}, {D.x} + {D.y}")
