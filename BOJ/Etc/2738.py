# Solved on 2022. 6. 25.
# 2738 행렬 덧셈

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr_a = [[*map(int, input().split())] for _ in range(N)]
arr_b = [[*map(int, input().split())] for _ in range(N)]
print(*map(lambda y: ' '.join(str(i) for i in y), [*map(lambda x: [*map(sum, zip(x[0], x[1]))], map(list, zip(arr_a, arr_b)))]), sep='\n')
