# Solved on 2022. 6. 15.
# 1822 차집합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if len(a-b):
    print(len(a-b))
    print(*sorted(a-b))
else:
    print(0)
