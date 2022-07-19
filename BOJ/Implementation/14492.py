# Solved on 2022. 7. 19.
# 14492 부울행렬의 부울곱

import sys
input = sys.stdin.readline

N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
brr = [[*map(int, input().split())] for _ in range(N)]

count = 0
for i in range(N):
    for j in range(N):
        for n in range(N):
            if arr[i][n] and brr[n][j] == 1:
                count += 1
                break
print(count)
