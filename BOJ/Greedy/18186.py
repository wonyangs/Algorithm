# Solved on 2022. 10. 15.
# 18186 라면 사기 (Large)

import sys
input = sys.stdin.readline

N, B, C = map(int, input().split())
arr = [*map(int, input().split())]
if B < C:
    C = B

b, c, d = B, B+C, B+C+C
res = [0, 0, 0]
info = [arr[0], 0, 0]
for i in range(1, N):
    n = arr[i]
    if n == 0:
        res[0] += info[0]
        res[1] += info[1]
        res[2] += info[2]
        info = [0, 0, 0]
        continue
    res[2] += info[2]
    info[2] = 0
    new_info = [0, 0, 0]

    if info[0] <= n:
        new_info[1] = info[0]
        n -= info[0]
        info[0] = 0
    else:
        new_info[1] = n
        info[0] -= n
        res[0] += info[0]
        res[1] += info[1]
        res[2] += info[2]
        info = new_info
        continue
    if info[1] <= n:
        new_info[2] = info[1]
        n -= info[1]
        info[1] = 0
    else:
        new_info[2] = n
        info[1] -= n
        res[0] += info[0]
        res[1] += info[1]
        res[2] += info[2]
        info = new_info
        continue

    if n > 0:
        new_info[0] = n
    info = new_info
res[0] += info[0]
res[1] += info[1]
res[2] += info[2]
print(res[0] * b + res[1] * c + res[2] * d)
