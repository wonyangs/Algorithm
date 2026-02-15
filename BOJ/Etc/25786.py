a = input()
b = input()
n = max(len(a), len(b))
a = a.zfill(n)
b = b.zfill(n)
res = ""

for i in range(n):
    x = int(a[i])
    y = int(b[i])
    if (x <= 2 and y <= 2) or (x >= 7 and y >= 7):
        res += "0"
    else:
        res += "9"

print(res)
