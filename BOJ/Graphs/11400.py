# Solved on 2022. 8. 23.
# 11400 단절선

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def dfs(n, cnt, parent):
    visit[n] = cnt
    ret = visit[n]

    for nxt in graph[n]:
        if nxt == parent:
            continue
        if visit[nxt] != 0:
            ret = min(ret, visit[nxt])
            continue
        subtree = dfs(nxt, cnt+1, n)
        ret = min(subtree, ret)

        if subtree > visit[n]:
            cut_line.add(tuple(sorted([n, nxt])))
    return ret


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visit = [0] * (V+1)
node = set()
cut_line = set()
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    node.add(a)
    node.add(b)
for n in node:
    if not visit[n]:
        dfs(n, 1, 0)
print(len(cut_line))
for a, b in sorted(cut_line):
    print(a, b)
