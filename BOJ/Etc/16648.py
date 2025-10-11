t, p = map(int, input().split())
if p > 20:
    r = (100 - p) / t
    print((p + 20) / r)
else:
    r = 2 * (60 - p) / t
    print(2 * p / r)
