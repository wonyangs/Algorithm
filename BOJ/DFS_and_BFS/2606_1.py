# Solved on 2021.01.03
# 2606 바이러스 ver.BFS

# ---------------------------

from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, n, visited):
    visited[n] = True
    queue = deque([n])
    count = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1

    return count


com_num = int(input())
n = int(input())
graph = [[] for _ in range(com_num+1)]
visited = [False] * (com_num+1)

for _ in range(n):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

count = bfs(graph, 1, visited)
print(count)
