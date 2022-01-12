# Solved on 2022. 1. 12.
# 2352 반도체 설계

import sys
input = sys.stdin.readline


def binarysearch(lis, num):
    start, end = 0, len(lis)
    
    while start < end:
        mid = (start+end) // 2
        if lis[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end


N = int(input())
arr = [*map(int, input().split())]

lis = [arr[0]]
for i in range(1, N):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        idx = binarysearch(lis, arr[i])
        lis[idx] = arr[i]
print(len(lis))
