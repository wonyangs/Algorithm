p = [float(input()) for _ in range(10)]
m = 0
for e in range(10):
    s = sorted([p[i] for i in range(10) if i != e], reverse=True)
    r = 1
    for i in range(9):
        r *= s[i] / (i + 1)
    m = max(m, r)
print(m * 1e9)
