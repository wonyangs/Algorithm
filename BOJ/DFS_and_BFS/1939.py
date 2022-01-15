# Solved on 2022. 1. 15.
# 1939 중량제한

from collections import deque
import sys
input = sys.stdin.readline


def bfs(weight):
    queue = deque()
    visit = [False] * (N+1)
    visit[S] = True
    queue.append(S)
    
    while queue:
        node = queue.popleft()
        if node == E:
            return True
            
        for nxt, w in graph[node]:
            if not visit[nxt] and w > weight:
                queue.append(nxt)
                visit[nxt] = True
    return False


def binarysearch():
    start, end = 1, int(10e9)
    while start < end:
        mid = (start+end)//2
        if bfs(mid):
            start = mid + 1
        else:
            end = mid
    return end


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
S, E = map(int, input().split())
print(binarysearch())
