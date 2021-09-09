# Solved on 2021. 09. 10.
# 1449 수리공 항승

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

count = 1
start = arr[0]

for i in range(1, N):
    if arr[i] - start >= L:
        count += 1
        start = arr[i]

print(count)
