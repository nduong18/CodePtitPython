from itertools import *
n = int(input())
digits = list('2357')
for length in range(4, n+1):
    for p in product(digits, repeat=length):
        s = "".join(p)
        if all(d in s for d in digits):
            if s[-1] in '357': print(s)

