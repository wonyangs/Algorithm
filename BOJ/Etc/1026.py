# Solved on 2022. 1. 1.
# 1026 보물

import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
A.sort()
A.reverse()
B.sort()
res = 0
for i in range(N):
    res += A[i] * B[i]
print(res)
