# Solved on 2022. 2. 1.
# 2644 촌수계산

from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    visit = [-1] * (N+1)
    visit[start] = 0
    
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if visit[nxt] == -1:
                visit[nxt] = visit[now] + 1
                queue.append(nxt)
    return visit[B]


N = int(input())
A, B = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(A))
