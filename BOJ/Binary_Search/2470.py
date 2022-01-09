# Solved on 2022. 1. 9.
# 2470 두 용액

import sys
input = sys.stdin.readline

N = int(input())

arr = [*map(int, input().split())]
arr.sort()
start, end = 0, N-1
res = 2000000000
x, y = -1, -1
while start < end:
    mid = arr[start] + arr[end]
    if abs(mid) < res:
        res = abs(mid)
        x, y = arr[start], arr[end]
    if mid < 0:
        start += 1
    else:
        end -= 1
print(x, y)
