import sys

v = sys.stdin.read().split()
if not v:
    exit()

n, m = int(v[0]), int(v[1])
d = {}
i = 2

for _ in range(n):
    s = v[i+1]
    k = v[i+2] + v[i+3] + v[i+4]
    if k in d:
        d[k].append(s)
    else:
        d[k] = [s]
    i += 9

for _ in range(m):
    k = v[i] + v[i+1] + v[i+2]
    if k in d:
        if len(d[k]) == 1:
            print(d[k][0])
        else:
            print('?')
    else:
        print('!')
    i += 3
