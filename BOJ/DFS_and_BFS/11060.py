# Solved on 2022. 6. 26.
# 11060 점프 점프

from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(0)
    visit = [-1] * N
    visit[0] = 0

    while queue:
        x = queue.popleft()
        if x == N - 1:
            print(visit[x])
            return
        for i in range(1, arr[x] + 1):
            nx = x + i
            if nx >= N:
                continue
            if visit[nx] == -1:
                visit[nx] = visit[x] + 1
                queue.append(nx)
    print(-1)


N = int(input())
arr = [*map(int, input().split())]
bfs()
