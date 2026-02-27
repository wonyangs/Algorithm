import sys

for l in sys.stdin:
    l = l.strip('\n')
    if l == '#':
        break
    r = []
    for w in l.split():
        if len(w) > 2:
            r.append(w[0] + w[1:-1][::-1] + w[-1])
        else:
            r.append(w)
    print(' '.join(r))
