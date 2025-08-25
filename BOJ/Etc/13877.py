import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    k, s = sys.stdin.readline().split()
    k = int(k)
    o = int(s, 8) if all(c in "01234567" for c in s) else 0
    d = int(s)
    h = int(s, 16)
    print(k, o, d, h)
