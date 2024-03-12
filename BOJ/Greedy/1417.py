import sys
import heapq

input = sys.stdin.readline

N = int(input())
dasom = int(input())
if N == 1:
    print(0)
    sys.exit(0)

heap = []
for _ in range(N - 1):
    heapq.heappush(heap, -int(input()))

cnt = 0
max_num = -heapq.heappop(heap)
while max_num >= dasom:
    dasom += 1
    heapq.heappush(heap, -max_num+1)
    max_num = -heapq.heappop(heap)
    cnt += 1
print(cnt)
