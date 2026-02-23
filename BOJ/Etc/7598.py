import sys

d = sys.stdin.read().splitlines()
i = 0
while i < len(d):
    t = d[i].strip()
    i += 1
    if not t:
        continue
    p = t.split()
    if p[0] == '#':
        break
    f = p[0]
    s = int(p[1])
    while i < len(d):
        t2 = d[i].strip()
        i += 1
        if not t2:
            continue
        p2 = t2.split()
        c = p2[0]
        v = int(p2[1])
        if c == 'X':
            print(f"{f} {s}")
            break
        if c == 'B' and s + v <= 68:
            s += v
        if c == 'C' and s >= v:
            s -= v
