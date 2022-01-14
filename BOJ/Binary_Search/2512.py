# Solved on 2022. 1. 14.
# 2512 예산

import sys
input = sys.stdin.readline


def binarysearch():
    start, end = 1, max(arr)
    while start <= end:
        mid = (start+end) // 2
        res = 0
        for n in arr:
            if n <= mid:
                res += n
            else:
                res += mid
        
        if res == M:
            return mid
        elif res < M:
            start = mid + 1
        else:
            end = mid - 1
    mid = (start+end) // 2
    return mid


N = int(input())
arr = [*map(int, input().split())]
M = int(input())
print(binarysearch())
