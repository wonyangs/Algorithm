import sys
d = sys.stdin.read().split()
n = int(d[0])
print(f"{sum(int(v) for v in d[3+2*n::2])/n:.5f}")
