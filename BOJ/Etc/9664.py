n = int(input())
o = int(input())
v = []
for r in range(min(n, o + 1)):
    if (o - r) % (n - 1) == 0:
        q = (o - r) // (n - 1)
        v.append(n * q + r)
print(min(v), max(v))
