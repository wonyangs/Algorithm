from collections import deque


def bfs(graph, N):
    queue = deque()
    visit = [-1] * (N + 1)

    visit[1] = 2
    queue.append(1)
    
    res = 0
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visit[n] != 0 and visit[i] == -1:
                visit[i] = visit[n] - 1
                queue.append(i)
                res += 1
    return res

N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

res = bfs(arr, N)

print(res)
