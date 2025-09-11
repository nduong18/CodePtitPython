n = int(input())
a = list(map(int, input().split()))
st = []
for i in a:
    if st and (st[-1] + i) % 2 == 0:
        st.pop()
    else:
        st.append(i)
print(len(st))