# Solved on 2022. 3. 7.
# 11003 최솟값 찾기

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [*map(int, input().split())]
queue = deque()
res = []
for i in range(N):
    while queue and queue[-1][1] > arr[i]:
        queue.pop()
    while queue and queue[0][0] < i-L+1:
        queue.popleft()
    
    queue.append((i, arr[i]))
    res.append(queue[0][1])
print(*res)
