import sys
d = sys.stdin.read().split()
i = 0
while i < len(d):
    n = int(d[i])
    i += 1
    if n == 0:
        break
    a = [int(x) for x in d[i:i+n]]
    i += n
    v = sum(a) / n
    c = sum(1 for x in a if x <= v)
    print(c)
