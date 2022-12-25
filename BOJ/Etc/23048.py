# Solved on 2022. 12. 25.
# 23048 자연수 색칠하기

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (N + 1)
arr[1] = 1
count = 1
for i in range(2, N + 1):
    if arr[i] == 0:
        count += 1
        for j in range(i, N + 1, i):
            arr[j] = count
print(count)
print(*arr[1:])
