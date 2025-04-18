import sys
for l in sys.stdin:
    d, m, y = map(int, l.split())
    if d == m == y == 0:
        break
    a = [31, 29 if y % 400 == 0 or (y % 4 == 0 and y % 100) else 28,
         31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(sum(a[:m - 1]) + d)
