import sys

data = [list(map(int, line.split())) for line in sys.stdin]
c, m = zip(*data)
c = list(c)
m = list(m)

for i in range(100):
    s = i % 3
    t = (i + 1) % 3
    p = min(m[s], c[t] - m[t])
    m[s] -= p
    m[t] += p

print(m[0])
print(m[1])
print(m[2])
