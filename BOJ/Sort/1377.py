# Solved on 2022. 2. 19.
# 1377 버블 소트

import sys
input = sys.stdin.readline   

N = int(input())
arr = [[int(input()), k] for k in range(N)]
sorted_arr = sorted(arr)
MAX = 0
for i in range(N):
    if arr[sorted_arr[i][1]][0] == sorted_arr[i][0]:
        MAX = max(MAX, sorted_arr[i][1]-i)
print(MAX + 1)
