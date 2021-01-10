# Solved on 2021.01.03
# 2606 바이러스 ver.DFS

# ---------------------------

import sys
input = sys.stdin.readline


def dfs(graph, n, visited):
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)


com_num = int(input())
n = int(input())
graph = [[] for _ in range(com_num+1)]
visited = [False] * (com_num+1)
count = 0

for _ in range(n):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

dfs(graph, 1, visited)

for i in visited:
    if visited[i]:
        count += 1

print(count-1)
