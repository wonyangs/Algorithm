import sys
a = sys.stdin.read().split()
n = int(a[0])
m = 0
for i in range(n - 1):
    x, y = int(a[2*i+1]), int(a[2*i+2])
    u, v = int(a[2*i+3]), int(a[2*i+4])
    s = (v - y) // (u - x)
    if s > m:
        m = s
print(m)
