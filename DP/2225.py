# Solved on 2021. 11. 08.
# 2225 합분해

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [[0] * N for _ in range(K)]

for i in range(N):
    arr[0][i] = 1
for i in range(1, K):
    arr[i][0] = i + 1
    for j in range(1, N):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]

print(arr[K-1][N-1] % 1000000000)
