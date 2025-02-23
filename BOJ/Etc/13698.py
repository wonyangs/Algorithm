x = input().strip()
c = ['S', '', '', 'B']
s = {'A': (0, 1), 'B': (0, 2), 'C': (0, 3), 'D': (1, 2), 'E': (1, 3), 'F': (2, 3)}
for m in x:
    i, j = s[m]
    c[i], c[j] = c[j], c[i]
print(c.index('S') + 1)
print(c.index('B') + 1)
