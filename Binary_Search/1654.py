# Solved on 2021. 12. 29.
# 1654 랜선 자르기

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start, end = 1, max(arr)
mid = (end+start)//2
MAX = 0
while start <= end:
    res = 0
    for n in arr:
        res += n // mid

    if res < N:
        end = mid - 1
        mid = (end+start)//2
    else:
        MAX = max(MAX, mid)
        start = mid + 1
        mid = (end+start)//2
print(MAX)
