a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

x = min(c, g) - max(a, e)
y = min(b, f) - max(d, h)

print(max(0, x) * max(0, y))
