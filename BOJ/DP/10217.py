# Solved on 2022. 3. 3.
# 10217 KCM Travel

import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(N, M):
    dp = [[INF]*(M+1) for _ in range(N+1)]
    dp[1][0] = 0

    for time in range(M+1):
        for n in range(1, N+1):
            dist = dp[n][time]
            if dist != INF:
                for nxt, nxt_c, nxt_d in graph[n]:
                    if time + nxt_c > M:
                        continue
                    dp[nxt][time+nxt_c] = min(dp[nxt][time+nxt_c], dist+nxt_d)

    return min(dp[N])


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    dist = dijkstra(N, M)
    if dist != INF:
        print(dist)
    else:
        print('Poor KCM')
