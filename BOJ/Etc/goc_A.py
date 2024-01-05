a, b, c, d, n = map(int, input().split())
avg = (a+b+c+d)
if n * 4 < avg:
    print(0)
else:
    print(n * 4 - avg)
