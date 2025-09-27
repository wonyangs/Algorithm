n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    if i == 0:
        x1, x2, y1, y2 = a, c, b, d
    else:
        x1 = min(x1, a)
        x2 = max(x2, c)
        y1 = min(y1, b)
        y2 = max(y2, d)
    print(2 * (x2 - x1 + y2 - y1))
