import sys

d = list(map(int, sys.stdin.read().split()))
it = iter(d)
n = next(it)
m = next(it)

t1 = 510000
t2 = 1020000
t3 = 1530000
t4 = 2040000

o = []
for _ in range(n):
    r = []
    for _ in range(m):
        R = next(it)
        G = next(it)
        B = next(it)
        I = 2126 * R + 7152 * G + 722 * B
        if I < t1:
            r.append('#')
        elif I < t2:
            r.append('o')
        elif I < t3:
            r.append('+')
        elif I < t4:
            r.append('-')
        else:
            r.append('.')
    o.append(''.join(r))

print('\n'.join(o))
