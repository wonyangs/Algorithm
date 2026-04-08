import sys
from collections import Counter

d = sys.stdin.read().split()
print("No" if max(Counter(d[1:]).values()) > 2 else "Yes")
