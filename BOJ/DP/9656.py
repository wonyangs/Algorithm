N = int(input())

dp = [False] * (1001)
dp[0] = False
dp[1] = False
dp[2] = True

for i in range(3, N + 1):
    dp[i] = not (dp[i - 1] or dp[i - 3])
print("SK" if dp[N] else "CY")
