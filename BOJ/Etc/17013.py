s = input()
h = s.count('H') % 2
v = s.count('V') % 2
g = [[1, 2], [3, 4]]
if h:
    g.reverse()
if v:
    g[0].reverse()
    g[1].reverse()
for r in g:
    print(*r)
