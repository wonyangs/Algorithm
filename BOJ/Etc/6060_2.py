import sys
d = sys.stdin.read().split()
print(sum(int(c) for c in d[3::3]) % 2)
