# Solved on 2022. 2. 25.
# 1922 네트워크 연결

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [*map(int, input().split())]

MAX = -1
res = 0
for i in range(K):
    res += arr[i]
MAX = max(MAX, res)

start = -1
n = K-1

for _ in range(N):
    n += 1
    start += 1
    n %= N
    start %= N
    res -= arr[start]
    res += arr[n]
    MAX = max(MAX, res)

print(MAX)
