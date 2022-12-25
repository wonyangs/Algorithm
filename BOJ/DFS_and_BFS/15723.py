# Solved on 2022. 12. 25.
# 15723 n단 논법

from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(start, end):
    queue = deque()
    visit = set()
    queue.append(start)
    visit.add(start)
    
    while queue:
        now = queue.popleft()
        if now == end:
            print("T")
            return
        
        for nxt in graph[now]:
            if nxt in visit:
                continue
            queue.append(nxt)
            visit.add(nxt)
    print("F")


graph = defaultdict(list)
for _ in range(int(input())):
    arr = input().split()
    graph[arr[0]].append(arr[2])
for _ in range(int(input())):
    arr = input().split()
    bfs(arr[0], arr[2])
