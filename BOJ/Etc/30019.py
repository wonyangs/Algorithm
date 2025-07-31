import sys
input = sys.stdin.readline

N, M = map(int, input().split())
t = [0] * (N + 1)
out = []

for _ in range(M):
    k, s, e = map(int, input().split())
    if s >= t[k]:
        out.append("YES")
        t[k] = e
    else:
        out.append("NO")

print("\n".join(out))
