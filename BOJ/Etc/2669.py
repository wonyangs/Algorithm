# Solved on 2022. 6. 17.
# 2669 직사각형 네개의 합집합의 면적 구하기

import sys
input = sys.stdin.readline

res = set()
for _ in range(4):
    ax, ay, bx, by = map(int, input().split())
    for i in range(ax, bx):
        for j in range(ay, by):
            res.add((i, j))
print(len(res))
