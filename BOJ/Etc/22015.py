arr = [*map(int, input().split())]
m = max(arr)
res = 0
for n in arr:
    res += m - n
print(res)
