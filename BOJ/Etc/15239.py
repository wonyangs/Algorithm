import sys

k = "+_)(*&^%$#@!./,;{}"
r = sys.stdin.readline

try:
    n = int(r())
    for _ in range(n):
        s = int(r())
        p = r().strip()

        if s < 12:
            print("invalid")
            continue

        a = b = c = d = 0
        for x in p:
            if x.islower(): a = 1
            elif x.isupper(): b = 1
            elif x.isdigit(): c = 1
            elif x in k: d = 1

        if a and b and c and d:
            print("valid")
        else:
            print("invalid")
except:
    pass
