from collections import deque
s = input().strip()
r = s.index('@')
b = s.index('#')
t = s.index('!')
dq = deque([(r, b, 0)])
vis = {(r, b)}
while dq:
    r, b, c = dq.popleft()
    if b == t:
        print(c)
        break
    for d in (-1, 1):
        nr = r + d
        if 0 <= nr < 10:
            if nr != b:
                if (nr, b) not in vis:
                    vis.add((nr, b))
                    dq.append((nr, b, c + 1))
            else:
                nb = b + d
                if 0 <= nb < 10 and (b, nb) not in vis:
                    vis.add((b, nb))
                    dq.append((b, nb, c + 1))
else:
    print(-1)
