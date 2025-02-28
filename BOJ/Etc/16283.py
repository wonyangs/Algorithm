import sys

data = sys.stdin.read().split()
a = int(data[0])
b = int(data[1])
n = int(data[2])
w = int(data[3])

sol = []
for s in range(1, n):
    g = n - s
    if a * s + b * g == w:
        sol.append((s, g))

if len(sol) == 1:
    print(sol[0][0], sol[0][1])
else:
    print(-1)
