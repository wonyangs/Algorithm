# Solved on 2022. 8. 25.
# 1182 부분수열의 합

from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = [*map(int, input().split())]
res = 0
for i in range(1, N+1):
    for com in combinations(arr, i):
        if sum(com) == S:
            res += 1
print(res)
