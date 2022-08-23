# Solved on 2022. 8. 23.
# 11266 단절점

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def dfs(n, cnt):
    visit[n] = cnt
    children = 0
    ret = visit[n]

    for nxt in graph[n]:
        if visit[nxt] != 0:
            ret = min(ret, visit[nxt])
        else:
            children += 1
            subtree = dfs(nxt, cnt+1)
            if cnt != 1 and subtree >= visit[n]:
                cut_node.add(n)
            ret = min(subtree, ret)
    if cnt == 1 and children >= 2:
        cut_node.add(n)
    return ret


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visit = [0] * (V+1)
cut_node = set()
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, V+1):
    if not visit[i]:
        dfs(i, 1)
print(len(cut_node))
print(*sorted(cut_node))
