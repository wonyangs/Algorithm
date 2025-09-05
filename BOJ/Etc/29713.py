from collections import Counter

input()
s = ''.join(input().split())
r = Counter('BRONZESILVER')
c = Counter(s)
print(min(c[k] // r[k] for k in r))
