# Solved on 2022. 3. 6.
# 10871 X보다 작은 수

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
for n in [*map(int, input().split())]:
    if n < X:
        print(n, end=' ')
