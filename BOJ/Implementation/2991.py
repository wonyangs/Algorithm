a, b, c, d = map(int, input().split())
arr = [*map(int, input().split())]

for n in arr:
    x = n % (a + b)
    y = n % (c + d)
    if 0 < x <= a and 0 < y <= c:
        print(2)
    elif 0 < x <= a or 0 < y <= c:
        print(1)
    else:
        print(0)
