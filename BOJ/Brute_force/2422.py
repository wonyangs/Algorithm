# Solved on 2022. 6. 22.
# 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = set(i for i in range(1, N+1))
ice_info = [[*map(int, input().split())] for _ in range(M)]
result = set()
for a, b in ice_info:
    for i in range(1, N+1):
        if i != a and i != b:
            result.add(tuple(sorted([a, b, i])))
print(len(list(combinations(arr, 3))) - len(result))
