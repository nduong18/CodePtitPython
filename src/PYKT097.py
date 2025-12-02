import sys
dau_cau = ".!?"
for line in sys.stdin:
    s = line.lower().strip().split()
    z = s[0].title()
    for i in range(1, len(s)):
        if i == len(s) - 1:
            if s[i] in dau_cau:
                z += s[i]
            else:
                if s[i][-1:] not in dau_cau:
                    z += " " + s[i] + "."
                else:
                    z += " " + s[i]
        else:
            z += " " + s[i]
    print(z)