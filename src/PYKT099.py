file1 = r"DATA1.in"
file2 = r"DATA2.in"

SET1 = set()
with open(file1) as f1:
    for line in f1:
        z = line.lower().strip().split()
        for i in z: SET1.add(i)

SET2 = set()
with open(file2) as f2:
    for line in f2:
        z = line.lower().strip().split()
        for i in z: SET2.add(i)

RES1 = sorted(SET1 - SET2)
RES2 = sorted(SET2 - SET1)
print(" ".join(RES1))
print(" ".join(RES2))


        