t = int(input())
i = 0
ds = []

while i < t:
    topic = input().strip()
    i += 1
    cnt = 0
    while i < t:
        line = input().strip()
        i += 1
        if line == "": break
        cnt += 1
    ds.append((topic, cnt))
for t,c in ds:
    print(f"{t}: {c}")