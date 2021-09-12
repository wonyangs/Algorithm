# Solved on 2021. 09. 12.
# 12851 숨바꼭질 2

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = max(n, k)


def bfs(start, graph):
    queue = deque()
    queue.append(start)
    graph[start] = 0
    count = 0

    while queue:
        v = queue.popleft()
        dv = [v-1, v+1, v*2]
        if v == k:
            count += 1

        for i in dv:
            if i < 0 or i >= num + 9:
                continue
            if graph[i] >= graph[v] + 1:
                graph[i] = graph[v] + 1
                queue.append(i)
    return count


graph = [100001] * (num + 10)
count = bfs(n, graph)

print(graph[k])
print(count)
