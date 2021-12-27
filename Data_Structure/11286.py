# Solved on 2021. 12. 27.
# 11286 절댓값 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if queue:
            num, val = heapq.heappop(queue)
            print(num * val)
        else:
            print(0)
    elif x > 0:
        heapq.heappush(queue, (x, 1))
    else:
        heapq.heappush(queue, (-x, -1))
