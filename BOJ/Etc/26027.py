import math

r = int(input())
m = float('inf')
ax, ay = 0, 0

for x in range(r + 1):
    y = int(math.sqrt(r*r - x*x)) + 1
    d = x*x + y*y
    if d < m:
        m = d
        ax, ay = x, y

print(ax, ay)
