import sys

it = list(map(int, sys.stdin.read().split()))
n = it[0]
p = it[1]
ans = 0
for a in it[2:2 + n]:
    d = abs(a - p)
    ans += min(d, 360 - d)
    p = a
print(ans)
