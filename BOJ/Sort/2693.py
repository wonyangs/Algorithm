# Solved on 2022. 5. 17.
# 2693 N번째 큰 수

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print([*reversed(sorted([*map(int, input().split())]))][2])
