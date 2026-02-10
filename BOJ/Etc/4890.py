import sys
import math

for s in sys.stdin:
    w, h = map(int, s.split())
    if w == 0 and h == 0:
        break
    g = math.gcd(w, h)
    print((w // g) * (h // g))
