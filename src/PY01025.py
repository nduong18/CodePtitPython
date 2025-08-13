x = input()
r = [x[max(0,i-3):i] for i in range(len(x), 0, -3)]
r.reverse()
print(",".join(r))