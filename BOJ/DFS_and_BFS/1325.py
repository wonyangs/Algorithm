# Solved on 2022. 3. 2.
# 1325 효율적인 해킹

from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    queue = deque()
    queue.append(n)
    visit = [False] * (N+1)
    visit[n] = True
    count = 1

    while queue:
        n = queue.popleft()
        for nxt in graph[n]:
            if not visit[nxt]:
                visit[nxt] = True
                queue.append(nxt)
                count += 1
    return count

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
res = []
MAX = -1
for i in range(1, N+1):
    cnt = bfs(i)
    if MAX < cnt:
        MAX = cnt
        res = [i]
    elif MAX == cnt:
        res.append(i)
print(*res)
