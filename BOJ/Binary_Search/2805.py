# Solved on 2022. 1. 2.
# 2805 나무 자르기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]

start, end = 0, max(arr)
while start <= end:
    mid = (start+end) // 2
    res = sum(i - mid if i > mid else 0 for i in arr)
    if res < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)
