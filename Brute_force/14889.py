# Solved on 2021. 12. 20.
# 14889 스타트와 링크

from itertools import combinations
import sys
input = sys.stdin.readline

def sumPoint(arr):
    res = 0
    for i in arr:
        for j in arr:
            res += graph[i][j]
    return res


N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]
com = list(combinations([i for i in range(0, N)], N//2))
arr = []
for i in range(0, len(com)//2):
    arr.append(abs(sumPoint(com[i]) - sumPoint(com[-i-1])))
print(min(arr))
