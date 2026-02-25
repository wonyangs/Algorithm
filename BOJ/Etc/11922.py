import sys
i = sys.stdin.read().split()
b = i[1]
d = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
u = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}
r = 0
for c in i[2:]:
    r += d[c[0]] if c[1] == b else u[c[0]]
print(r)
