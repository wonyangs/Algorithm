# Solved on 2021. 12. 09.
# 9252 LCS 2

import sys
input = sys.stdin.readline

arrA = list(input().strip())
arrB = list(input().strip())

dp = [[0] * (len(arrA)+1) for _ in range(len(arrB)+1)]
for i in range(1, len(arrB)+1):
    for j in range(1, len(arrA)+1):
        if arrA[j-1] == arrB[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
x, y = len(arrB), len(arrA)
arr = []
while dp[x][y] != 0:
    if dp[x][y] == dp[x-1][y] + 1 and dp[x][y] == dp[x][y-1] + 1:
        arr.append(arrB[x-1])
        x -= 1
        y -= 1
    else:
        if dp[x][y-1] > dp[x-1][y]:
            y -= 1
        else:
            x -= 1
arr.reverse()
print(dp[-1][-1])
for n in arr:
    print(n, end='')
print()
