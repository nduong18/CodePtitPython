n = int(input())
arr = list(map(float,input().split()))
min_value = min(arr)
max_value = max(arr)

arr1 = []
for i in arr:
    if (i != min_value and i != max_value):
        arr1.append(i)

result = sum(arr1) / len(arr1)
print(round(result,2))