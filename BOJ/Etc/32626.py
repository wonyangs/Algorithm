import sys
input = sys.stdin.readline

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
px, py = map(int, input().split())

def btw(a, b, c):
    return min(a, b) < c < max(a, b)

if sx == ex:
    print(2 if px == sx and btw(sy, ey, py) else 0)
elif sy == ey:
    print(2 if py == sy and btw(sx, ex, px) else 0)
else:
    a = (py == sy and btw(sx, ex, px)) or (px == ex and btw(sy, ey, py))
    b = (px == sx and btw(sy, ey, py)) or (py == ey and btw(sx, ex, px))
    print(2 if a and b else 1)
