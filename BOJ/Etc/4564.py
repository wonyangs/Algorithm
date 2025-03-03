import sys
for l in sys.stdin.read().splitlines():
    if l == "0": break
    s = l
    r = [s]
    while len(s) > 1:
        p = 1
        for c in s:
            p *= int(c)
        s = str(p)
        r.append(s)
    print(" ".join(r))
