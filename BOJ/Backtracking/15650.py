# Solved on 2021. 01. 12.
# 15650 N과 M (2)

from itertools import combinations
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

a = list(combinations(range(1, n+1), m))

for result in a:
    for num in result:
        print(num, end=' ')
    print()
