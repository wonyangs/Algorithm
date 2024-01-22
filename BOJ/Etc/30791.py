arr = [*map(int, input().split())]

a = arr[0]
res = 0
for n in arr[1:]:
    if a - n <= 1000:
        res += 1
print(res)
