# Solved on 2021. 01. 11.
# 1927 최소 힙

import heapq
import sys
input = sys.stdin.readline


n = int(input())
L = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if not L:
            print(0)
        else:
            print(heapq.heappop(L))
    else:
        heapq.heappush(L, x)
