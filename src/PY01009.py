x = input()
lower = 0
upper = 0
for c in x:
    if c.islower():
        lower += 1
    else:
        upper += 1
if (lower >= upper): 
    print(x.lower())
else:
    print(x.upper())
