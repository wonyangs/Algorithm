g = {c: (i // 4, i % 4) for i, c in enumerate("ABCDEFGHIJKLMNO")}
s = 0
for r in range(4):
    l = input().rstrip()
    for c, ch in enumerate(l):
        if ch != ".":
            a, b = g[ch]
            s += abs(a - r) + abs(b - c)
print(s)
