a, b = map(int, input().split())
c, d = map(int, input().split())
o = max(0, min(b, d) - max(a, c))
print((b - a) + (d - c) - o)
