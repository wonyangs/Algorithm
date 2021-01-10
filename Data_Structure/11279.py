# Solved on 2021. 01. 10.
# 11279 최대 힙

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    input_num = int(input())
    if input_num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, input_num * -1)
