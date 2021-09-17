# Solved on 2021. 09. 17.
# 13549 숨바꼭질 3

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

maxNum = 100001
queue = deque()
visited = [False] * maxNum
graph = [-1] * maxNum

graph[n] = 0
visited[n] = True
queue.append(n)

while queue:
    x = queue.popleft()
    
    if (x * 2) < maxNum and visited[x*2] == False:
        queue.appendleft(x*2)
        visited[x*2] = True
        graph[x*2] = graph[x]
        
    if (x + 1) < maxNum and visited[x+1] == False:
        queue.append(x+1)
        visited[x+1] = True
        graph[x+1] = graph[x] + 1

    if (x - 1) >= 0 and visited[x-1] == False:
        queue.append(x-1)
        visited[x-1] = True
        graph[x-1] = graph[x] + 1

print(graph[k])
