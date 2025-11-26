x, y = map(int, input().split())
p, d, s = x, 0, 1
while 1:
    t = x + s
    if min(p, t) <= y <= max(p, t):
        print(d + abs(y - p))
        break
    d += abs(t - p)
    p = t
    s *= -2
