import sys
d = sys.stdin.read().split()
m = int(d[1])
c = chr(64 + m)
print(sum(len(set(w)) == len(w) and max(w) <= c for w in d[2:]))
