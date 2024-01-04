import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque()
    dx = [-1, 1, -10, 10, 60]
    
    x, log = 0, [0, 0, 0, 0, 0]
    queue.append((x, log))
    
    MAX = 71
    visit = [False] * MAX
    arr = [-1] * MAX

    while queue:
        x, log = queue.popleft()
        
        if x >= 0 and x <= 60 and visit[x] is False:
            visit[x] = True
            arr[x] = log
            for i in range(5):
                nlog = [t for t in log]
                nlog[i] += 1
                queue.append((x + dx[i], nlog))
    
    return arr


arr = bfs()
for _ in range(int(input())):
    N = int(input())
    res = arr[N % 60][::-1]
    res[0] += N // 60
    print(*res)
