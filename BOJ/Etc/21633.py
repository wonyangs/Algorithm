N = int(input())
res = 25 + N / 100
if res < 100:
    res = 100
elif res > 2000:
    res = 2000
print("%.2f"%res)
