# Solved on 2021. 12. 24.
# 18258 큐 2

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    arr = list(input().split())
    cmd = arr[0]
    if cmd == "push":
        queue.append(arr[1])
    elif cmd == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
