# Solved on 2021. 01. 12.
# 7662 이중 우선순위 큐

import heapq
import sys
input = sys.stdin.readline


t = int(input())  # t = 테스트 데이터 개수

for _ in range(t):
    k = int(input())  # k = 연산의 개수
    i = 0
    min_heap, max_heap = [], []
    visited = [False] * 1000001

    for _ in range(k):
        input_data = input().split()

        cmd = input_data[0]
        num = int(input_data[1])

        if cmd == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
            i += 1
        else:  # cmd == 'D'
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:  # num == -1
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
