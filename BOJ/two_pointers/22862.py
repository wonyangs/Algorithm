# Solved on 2022. 3. 15.
# 22862 가장 긴 짝수 연속한 부분 수열 (large)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [*map(int, input().split())]

start, end = 0, 1
odd, even = 0, 0
if arr[start] % 2 == 0:
    even += 1
else:
    odd += 1

if N == 1:
    print(even)
    sys.exit(0)

if arr[end] % 2 == 0:
    even += 1
else:
    odd += 1

MAX = even
while start < end:
    if end+1 < N and odd <= K:
        end += 1
        if arr[end] % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        if arr[start] % 2 == 0:
            even -= 1
        else:
            odd -= 1
        start += 1
    
    MAX = max(MAX, even)

print(MAX)
