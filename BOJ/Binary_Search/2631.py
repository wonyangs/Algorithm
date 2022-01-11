# Solved on 2022. 1. 11.
# 2631 줄세우기

import sys
input = sys.stdin.readline


def binarySearch(lis, num):
    start, end = 0, len(lis)-1
    
    while start < end:
        mid = (start+end) // 2
        if lis[mid] < num:
            start = mid+1
        else:
            end = mid
    return end


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

lis = [arr[0]]
count = 1
while count < N:
    if lis[-1] < arr[count]:
        lis.append(arr[count])
    else:
        idx = binarySearch(lis, arr[count])
        lis[idx] = arr[count]
    count += 1
print(N-len(lis))
