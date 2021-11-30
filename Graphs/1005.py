# Solved on 2021. 11. 30.
# 1005 ACM Craft

import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    buildTime = [0] + list(map(int, input().split()))
    nodeNum = [0] * (N+1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        nodeNum[b] += 1
    W = int(input())

    queue = []
    for i in range(1, N+1):
        if nodeNum[i] == 0:
            heapq.heappush(queue, (buildTime[i], i))

    while queue:
        time, now = heapq.heappop(queue)
        if now == W:
            print(time)
            break
        changeNum = []
        for n in graph[now]:
            nodeNum[n] -= 1
            if nodeNum[n] == 0:
                changeNum.append(n)
        for n in changeNum:
            heapq.heappush(queue, (time + buildTime[n], n))
