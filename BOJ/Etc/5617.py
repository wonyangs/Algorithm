import sys
t = r = a = o = 0
for s in sys.stdin:
    if not s.strip():
        continue
    x, y, z = sorted(map(int, s.split()))
    if x + y <= z:
        break
    t += 1
    i, j = x * x + y * y, z * z
    if i == j:
        r += 1
    elif i > j:
        a += 1
    else:
        o += 1
print(t, r, a, o)
