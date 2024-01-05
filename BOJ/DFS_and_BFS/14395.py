from collections import deque


def bfs(S, T):
    if S == T:
        return "0"

    MAX = 1_000_000_001
    queue = deque()
    visit = set()
    
    log = ""
    queue.append((S, log))
    
    while queue:
        n, log = queue.popleft()
        
        if n == T:
            return log
        
        if n < 0 or n > MAX or n in visit:
            continue
        
        visit.add(n)
        queue.append((n * n, log + "*"))
        queue.append((n + n, log + "+"))
        queue.append((0, log + "-"))
        if n != 0:
            queue.append((1, log + "/"))
    
    return "-1"


S, T = map(int, input().split())
print(bfs(S, T))
