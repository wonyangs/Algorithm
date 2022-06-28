# Solved on 2022. 6. 29.
# 6118 숨바꼭질

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(1)
    visit = [-1] * (N + 1)
    visit[1] = 0
    max_idx = 1
    max_num = 0
    count = 1

    while queue:
        x = queue.popleft()
        if max_num < visit[x]:
            max_num = visit[x]
            count = 1
            max_idx = x
        elif max_num == visit[x]:
            count += 1
            if max_idx > x:
                max_idx = x

        for nx in graph[x]:
            if visit[nx] == -1:
                visit[nx] = visit[x] + 1
                queue.append(nx)
    print(max_idx, max_num, count)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs()
