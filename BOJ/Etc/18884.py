import sys
d = sys.stdin.read().split()
n, m = int(d[0]), int(d[1])
s = d[2:n+2]
t = d[n+2:n+m+2]
for x in d[n+m+3:]:
    v = int(x) - 1
    print(s[v%n] + t[v%m])
