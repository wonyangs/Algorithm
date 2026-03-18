import sys
d = list(map(int, sys.stdin.read().split()))
f = lambda x: x if x > 0 else x + 1
c = 1
for i in range(d[0]):
    c += f(d[i*2+2]) - f(d[i*2+1])
print(c if c > 0 else c - 1)
