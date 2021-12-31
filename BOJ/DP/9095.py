# Solved on 2020.12.22
# 9095 1, 2, 3 더하기

# ---------------------------

import sys
input = sys.stdin.readline


def main():
    dp = [1, 2, 4]

    for i in range(3, 12):
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])

    n = int(input())

    for _ in range(n):
        num = int(input())
        print(dp[num-1])


main()
