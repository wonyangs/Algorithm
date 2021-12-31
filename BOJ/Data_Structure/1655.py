# Solved on 2021. 12. 28.
# 1655 가운데를 말해요

import heapq
import sys
input = sys.stdin.readline

N = int(input())

MIN, MAX = [], []
mid = 0

for i in range(N):
    n = int(input())
    if i == 0:
        heapq.heappush(MAX, -n)
        mid = n
    else:
        if n > mid:
            if len(MAX) > len(MIN):
                heapq.heappush(MIN, n)
            else:
                heapq.heappush(MIN, n)
                heapq.heappush(MAX, -heapq.heappop(MIN))
                mid = -heapq.heappop(MAX)
                heapq.heappush(MAX, -mid)
        else:
            if len(MAX) > len(MIN):
                heapq.heappush(MAX, -n)
                heapq.heappush(MIN, -heapq.heappop(MAX))
                mid = -heapq.heappop(MAX)
                heapq.heappush(MAX, -mid)
            else:
                heapq.heappush(MAX, -n)
    
    print(mid)
