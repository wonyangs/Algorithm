import sys

for l in sys.stdin.read().splitlines():
    if l == '#':
        break
    s = ord(l[-1]) - 65
    r = []
    for c in l[:-1]:
        if c.isalpha():
            b = 65 if c.isupper() else 97
            r.append(chr((ord(c) - b - s) % 26 + b))
        else:
            r.append(c)
    print("".join(r))
