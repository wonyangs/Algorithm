N = int(input())
dp = [0] * (N + 1)

for h in range(2, N + 1):
    for s in range(1, h):
        dp[h] = max(dp[h], dp[s] + dp[h - s] + s * (h - s))

print(dp[N])
