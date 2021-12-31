# Solved on 2021. 10. 06.
# 13023 ABCDE

import sys
input = sys.stdin.readline


def dfs(visited, start, count):
    if count == 4:
        return True

    tmp = []
    for n in graph[start]:
        if n not in visited:
            tmp.append(n)

    for n in tmp:
        if dfs(set.union(visited, {start}), n, count+1):
            return True

    return False


N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


result = False
for i in range(N):
    visited = set()
    if dfs(visited, i, 0):
        result = True
        break

if result:
    print(1)
else:
    print(0)
