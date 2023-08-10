a, b = input().split()
res = 0
for i in a:
    for j in b:
        res += int(i) * int(j)
print(res)
