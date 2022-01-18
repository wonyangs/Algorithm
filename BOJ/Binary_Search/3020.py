# Solved on 2022. 1. 18.
# 3020 개똥벌레

import sys
input = sys.stdin.readline


def binarysearch(n, arr):
    if n > arr[-1]:
        return 0

    start, end = 0, N//2-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] < n:
            start = mid + 1
        else:
            end = mid
    return len(arr) - end


N, H = map(int, input().split())
down, up = [], []
for i in range(N):
    n = int(input())
    if i % 2 == 0:
        down.append(n)
    else:
        up.append(H-n)
down.sort()
up.sort()

MIN = int(1e9)
count = 1
arr = []
for i in range(1, H+1):
    res = 0
    res += binarysearch(i, down)
    res += len(up) - binarysearch(i, up)
    arr.append(res)
    if MIN > res:
        MIN = res
        count = 1
    elif MIN == res:
        count += 1
print(MIN, count)
