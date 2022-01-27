# Solved on 2022. 1. 27.
# 14501 퇴사

import sys
input = sys.stdin.readline

N = int(input())
plan = [[*map(int, input().split())] for _ in range(N)]

dp = set()
dp.add((0, 0))
for i in range(N):
    T, P = plan[i][0], plan[i][1]
    for t, p in list(dp):
        if t < i+1:
            dp.add((i+T, p+P))

MAX = -1
for t, p in list(dp):
    if t <= N:
        MAX = max(MAX, p)
print(MAX)
