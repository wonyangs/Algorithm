# Solved on 2022. 3. 16.
# 2230 수 고르기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start, end = 0, 0
MIN = float('INF')
while end < N and start <= end:
    if abs(arr[end] - arr[start]) < M:
        end += 1
    else:
        MIN = min(MIN, abs(arr[end] - arr[start]))
        start += 1
print(MIN)
