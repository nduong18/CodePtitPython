ds = []
t = int(input())
i = 0
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

for topic, c in ds:
    print(f"{topic}: {c}")