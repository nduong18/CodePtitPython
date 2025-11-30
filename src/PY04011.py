class ThanhVien:
    def __init__(self, ten1, ss, ten2):
        self.ten = ten1
        if ss == '>':
            self.nhoHon = ten2
        elif ss == '<':
            self.lonHon = ten2

t = int(input())
ds = list()

