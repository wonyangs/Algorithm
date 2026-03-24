import sys

d = sys.stdin.read().split()
c = {}
for x in d[1:]:
    k = int(x)
    c[k] = c.get(k, 0) + 1
m = max(c.values())
print(min(k for k, v in c.items() if v == m))
