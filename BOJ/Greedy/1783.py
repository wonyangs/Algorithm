# Solved on 2022. 7. 22.
# 1783 병든 나이트

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M + 1)//2))
elif M <= 6:
    print(min(4, M))
else:
    print(M - 2)
