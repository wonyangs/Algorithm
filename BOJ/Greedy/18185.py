# Solved on 2022. 10. 14.
# 18185 라면 사기 (Small)

import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]

res = 0
info = [arr[0], 0, 0]
for i in range(1, N):
    n = arr[i]
    if n == 0:
        res += info[0] * 3 + info[1] * 5 + info[2] * 7
        info = [0, 0, 0]
        continue
    res += info[2] * 7
    info[2] = 0
    new_info = [0, 0, 0]

    if info[0] <= n:
        new_info[1] = info[0]
        n -= info[0]
        info[0] = 0
    else:
        new_info[1] = n
        info[0] -= n
        res += info[0] * 3 + info[1] * 5 + info[2] * 7
        info = new_info
        continue
    if info[1] <= n:
        new_info[2] = info[1]
        n -= info[1]
        info[1] = 0
    else:
        new_info[2] = n
        info[1] -= n
        res += info[0] * 3 + info[1] * 5 + info[2] * 7
        info = new_info
        continue

    if n > 0:
        new_info[0] = n
    info = new_info
res += info[0] * 3 + info[1] * 5 + info[2] * 7
print(res)
