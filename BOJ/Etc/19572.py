a, b, c = map(int, input().split())
x = (a + b - c) / 2
y = (c + a - b) / 2
z = (b + c - a) / 2
if x <= 0 or y <= 0 or z <= 0:
    print(-1)
else:
    print(1)
    print(round(x, 1), round(y, 1), round(z, 1))
