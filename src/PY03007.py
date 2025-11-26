import re
doc = ''
while True:
    try: doc += input()
    except: break

s = re.split('[.?!]', doc)
for i in s:
    if len(i) == 0: continue
    i = i.lower().split()
    i[0] = i[0].title()
    print(' '.join(i))