# Solved on 2021. 10. 05.
# 9019 DSLR

from collections import deque
import sys
input = sys.stdin.readline


def Lrotate(n):
    first = n // 1000
    n %= 1000
    return n * 10 + first


def Rrotate(n):
    last = n % 10
    n //= 10
    return last * 1000 + n


def bfs(start, end):
    visited = set()
    queue = deque()
    queue.append((start, ""))
    visited.add(start)

    while queue:
        now, arr = queue.popleft()

        if now == end:
            print(arr)
            return

        # D 연산
        tmp = (now*2) % 10000
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, arr+"D"))
        # S 연산
        tmp = (now + 9999) % 10000
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, arr+"S"))
        # L 연산
        tmp = Lrotate(now)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, arr+"L"))
        # R 연산
        tmp = Rrotate(now)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, arr+"R"))


T = int(input())

for _ in range(T):
    start, end = map(int, input().split())
    bfs(start, end)
