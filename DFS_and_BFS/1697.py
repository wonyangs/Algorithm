# Solved on 2021. 01. 10.
# 1697 숨바꼭질

from collections import deque
import sys
input = sys.stdin.readline


def BFS(n, k, visited):
    count = 0
    if n == k:
        return count

    move = [n-1, n+1, n*2]
    visited[n] = count
    queue = deque()
    queue.append(move)

    while queue:
        move = []
        v = queue.popleft()
        count += 1

        for i in v:
            if i < 0 or i > 100000:
                continue

            if visited[i] == 0 and i != n:
                visited[i] = count
                if i == k:
                    return count
                move.append(i-1)
                move.append(i+1)
                move.append(i*2)

        queue.append(move)


n, k = map(int, input().split())

visited = [0 for _ in range(100001)]

print(BFS(n, k, visited))
