import sys

input = sys.stdin.readline


N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

dp = [[10001] * (K + 1) for _ in range(N)]

for idx in range(N):
    n = arr[idx]
    if idx == 0:
        for i in range(K + 1):
            if i % n == 0:
                dp[0][i] = i // n
        continue
    
    for i in range(K + 1):
        if i < n:
            dp[idx][i] = dp[idx-1][i]
        else:
            dp[idx][i] = min(dp[idx-1][i], dp[idx][i-n] + 1)

if dp[-1][-1] == 10001:
    print(-1)
else:
    print(dp[-1][-1])
