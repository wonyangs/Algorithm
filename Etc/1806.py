# Solved on 2021. 12. 02.
# 1806 부분합

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [arr[0]]

for i in range(1, N):
    prefix.append(prefix[-1] + arr[i])

start, end = 0, 0
MIN = 100000
while start < N and end < N:
    if prefix[end] >= S and end + 1 < MIN:
        MIN = end + 1
    if prefix[end] - prefix[start] >= S:
        if end != start and (end-start) < MIN:
            MIN = end-start
        start += 1
    else:
        end += 1
if MIN == 100000:
    print(0)
else:
    print(MIN)
