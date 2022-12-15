arr = map(int, input().split())

res = True
for n in arr:
    if n == 1 or n == 0:
        continue
    res = False
print("S" if res else "F")
