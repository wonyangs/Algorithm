import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = [*map(int, input().split())]
    target = int(input())
    
    dp = [[0] * (target + 1) for _ in range(N + 1)]
    
    for i, coin in enumerate(coins):
        for n in range(0, target+1):
            if n % coin == 0 and n != 0:
                dp[i+1][n] += 1
            for j in range(n, 0, -coin):
                dp[i+1][n] += dp[i][j]
    
    print(dp[-1][-1])
