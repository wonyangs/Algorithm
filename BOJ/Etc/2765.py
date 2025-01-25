import sys, math

p = 3.1415927
c = 0

for l in sys.stdin:
    d, r, t = map(float, l.split())
    if r == 0:
        break
    c += 1
    x = d * p * r / 63360
    y = x / (t / 3600)
    print(f"Trip #{c}: {x:.2f} {y:.2f}")
