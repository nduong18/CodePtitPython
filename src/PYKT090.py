res = []
filename = r"CONTACT.in"
with open(filename) as file_obj:
    for line in file_obj:
        r = line.lower().strip()
        if r not in res:
            res.append(r)
res = sorted(res)
for i in res: print(i)