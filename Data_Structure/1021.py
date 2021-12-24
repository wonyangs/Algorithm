# Solved on 2021. 12. 24.
# 1021 회전하는 큐

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]
arr = arr[::-1]
queue = deque()
for i in range(1, N+1):
    queue.append(i)
count = 0
while arr:
    if queue[0] == arr[-1]:
        queue.popleft()
        arr.pop()
    elif queue.index(arr[-1]) <= len(queue) // 2:
        queue.rotate(-1)
        count += 1
    else:
        queue.rotate(1)
        count += 1
print(count)
