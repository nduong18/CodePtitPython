from itertools import permutations
x = input()
for p in permutations(x):
    print("".join(p))