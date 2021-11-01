# Solved on 2021. 11. 01.
# 1966 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    queue = deque()
    N, M = map(int, input().split())
    values = list(map(int, input().split()))

    for i in range(len(values)):
        queue.append((values[i], i))

    values.sort()
    count = 0
    while queue:
        if queue[0][0] < values[-1]:
            num = queue.popleft()
            queue.append(num)
        else:
            count += 1
            val, num = queue.popleft()
            values.pop()
            if num == M:
                print(count)
                break
