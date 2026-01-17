import sys

while True:
    l = sys.stdin.readline()
    if not l: break
    a, b = l.split()
    if a == '#': break
    n = int(sys.stdin.readline())
    x = 0
    y = 0
    for _ in range(n):
        u, v = sys.stdin.readline().split()
        if u == v:
            x += 1
        else:
            y += 1
    print(a, x, b, y)
