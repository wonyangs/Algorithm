# Solved on 2022. 5. 27.
# 10797 10부제

import sys
input = sys.stdin.readline

N = int(input())
print([*map(int, input().split())].count(N))
