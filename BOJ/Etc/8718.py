x, k = map(int, input().split())
a, b, c = 0, 0, 0
if 7000 * k <= 1000 * x: a = 7000 * k
if 3500 * k <= 1000 * x: b = 3500 * k
if 1750 * k <= 1000 * x: c = 1750 * k
print(max(a, b, c))
