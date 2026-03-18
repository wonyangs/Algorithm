import sys

d = sys.stdin.read().split()
if not d:
    exit()
n = int(d[0])
v = [(int(d[i]), int(d[i+1])) for i in range(1, len(d), 2)]
r = 0

for i in range(n):
    c = [0] * 1000
    for j in range(n):
        if i != j:
            for k in range(v[j][0], v[j][1]):
                c[k] = 1
    r = max(r, sum(c))

print(r)
