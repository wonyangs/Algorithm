import sys

d = sys.stdin.read().split()
g = "".join(d[2:])

s = g.count('S')
e = g.count('E')
w = g.count('#')
a = g.count('A')
v = g.count('V')
o = sum(g.count(c) for c in "UDLR")

if s != 1 or e != 1:
    print(-1)
elif w <= 1 and o <= 1 and a == 0 and v == 0:
    print(1)
elif a == 0 and v == 0:
    print(2)
elif a == 0:
    print(3)
else:
    print(4)
