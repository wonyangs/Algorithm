# Solved on 2021. 09. 21.
# 16953 A → B

from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().split())


def bfs(start):
    queue = deque()
    queue.append([start, 1])
    MIN = int(1e9)
    
    while queue:
        now, count = queue.pop()
        if now == B and MIN > count:
            MIN = count

        array = [now * 10 + 1, now * 2]
        
        for i in array:
            if i <= B:
                queue.append([i, count+1])

    if MIN != int(1e9):
        return MIN
    else:
        return -1


print(bfs(A))
