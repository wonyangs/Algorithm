import sys
from collections import Counter

d = sys.stdin.read().split()
c = Counter(d[1:])
print(max(c.values()))
