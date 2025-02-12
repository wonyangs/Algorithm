import sys
I = sys.stdin.read().split()
n, m = map(int, I[:2])
b = [0] + list(map(int, I[2:2+n]))
p = 1
i = 0
for r in map(int, I[2+n:]):
    i += 1
    p += r
    if p >= n: break
    p += b[p]
    if p >= n: break
print(i)
