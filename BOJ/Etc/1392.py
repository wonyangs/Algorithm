N, Q = map(int, input().split())
s, q = [int(input()) for _ in range(N)], [int(input()) for _ in range(Q)]
t = [0] * (N + 1)
for i in range(1, N + 1): t[i] = t[i - 1] + s[i - 1]
print("\n".join(str(next(i for i in range(1, N + 1) if t[i - 1] <= x < t[i])) for x in q))
