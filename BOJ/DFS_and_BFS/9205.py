# Solved on 2022. 2. 7.
# 9205 맥주 마시면서 걸어가기

from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, store, end):
    queue = deque()
    queue.append(start)
    visit = [False] * len(store)
    
    happy = False
    while queue:
        x, y = queue.popleft()
        if abs(x-end[0]) + abs(y-end[1]) <= 1000:
            happy = True
            break
        
        for i in range(len(store)):
            if not visit[i] and abs(x - store[i][0]) + abs(y - store[i][1]) <= 1000:
                visit[i] = True
                queue.append(store[i])
    return happy


T = int(input())

for _ in range(T):
    N = int(input())
    home = [*map(int, input().split())]
    store = [[*map(int, input().split())] for _ in range(N)]
    festival = [*map(int, input().split())]
    if bfs(home, store, festival):
        print("happy")
    else:
        print("sad")
