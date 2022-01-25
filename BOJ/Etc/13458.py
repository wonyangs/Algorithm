# Solved on 2022. 1. 25.
# 13458 시험 감독

import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
B, C = map(int, input().split())
count = 0
for i in range(N):
    arr[i] -= B
    count+=1
    if arr[i] > 0:
        count += arr[i] // C
        if arr[i] % C != 0:
            count+=1
print(count)
