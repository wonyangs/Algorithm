import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = [tuple([*map(int, input().split())]) for _ in range(N)]
arr.sort()

heap = []
for a, b in arr:
    heapq.heappush(heap, b)
    top = heapq.heappop(heap)
    if top > a:
        heapq.heappush(heap, top)
print(len(heap))
