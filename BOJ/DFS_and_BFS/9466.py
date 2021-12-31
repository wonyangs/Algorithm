# Solved on 2021. 11. 21.
# 9466 텀 프로젝트

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def dfs(now):
    if now in visit or canTeam[now] != -1:
        return now
    visit.add(now)
    n = dfs(graph[now])
    if n in visit:
        visit.remove(now)
        canTeam[now] = 1
        return n
    else:
        visit.remove(now)
        canTeam[now] = 0
        return n


T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    canTeam = [-1] * (N+1)
    for i in range(1, N+1):
        if canTeam[i] != -1:
            continue
        visit = set()
        dfs(i)
    res = 0
    for i in range(1, N+1):
        if canTeam[i] == 0:
            res += 1
    print(res)
