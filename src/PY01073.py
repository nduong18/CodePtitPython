import itertools
x = input()
l = list(itertools.permutations(x))
for i in l:
    for j in i:
        print(j, end="")
    print()