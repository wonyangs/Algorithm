input()
arr = [*map(int, input().split())]
count = 1
res = 0
for n in arr:
    if n == 0:
        count = 1
    else:
        res += count
        count += 1
print(res)
