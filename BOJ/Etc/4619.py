import sys

for l in sys.stdin:
    b, n = map(int, l.split())
    if b == 0 and n == 0:
        break
    a = int(b ** (1 / n))
    print(a + 1 if abs((a + 1) ** n - b) < abs(a ** n - b) else a)
