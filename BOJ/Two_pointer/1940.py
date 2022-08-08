# Solved on 2022. 8. 8.
# 1940 주몽

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = sorted([*map(int, input().split())])

i, j, cnt = 0, N - 1, 0
while i < j:
    if arr[i] + arr[j] == M:
        cnt += 1
    if arr[i] + arr[j] < M:
        i += 1
    else:
        j -= 1
print(cnt)
