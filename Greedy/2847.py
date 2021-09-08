# Solved on 2021. 09. 08.
# 2847 게임을 만든 동준이

import sys
input = sys.stdin.readline

n = int(input())
arr = []
count = 0

for i in range(n):
    arr.append(int(input()))

arr.reverse()

for i in range(1, n):
    if arr[i-1] <= arr[i]:
        count += arr[i] - arr[i-1] + 1
        arr[i] = arr[i-1] - 1

print(count)
