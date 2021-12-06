# Solved on 2021. 12. 06.
# 2467 용액

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1
MIN = int(10e9)
a, b = -1, -1
while end-start > 0:
    if arr[start] + arr[end] > 0:
        if abs(arr[start] + arr[end]) < MIN:
            MIN = abs(arr[start] + arr[end])
            a = arr[start]
            b = arr[end]
        end -= 1
    elif arr[start] + arr[end] < 0:
        if abs(arr[start] + arr[end]) < MIN:
            MIN = abs(arr[start] + arr[end])
            a = arr[start]
            b = arr[end]
        start += 1
    else:
        a = arr[start]
        b = arr[end]
        break
print(a, b)
