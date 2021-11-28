# Solved on 2021. 11. 28.
# 2342 Dance Dance Revolution

from collections import deque
import sys
input = sys.stdin.readline


def sortNum(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

    
def addQ(nextq, goal, num, power):
    now = sortNum(goal, num)
    if now in nextq:
        if nextq[now] > power:
            nextq[now] = power
    else:
        nextq[now] = power
    return nextq


order = list(map(int, input().split()))
order = order[:-1]

queue = deque()
queue.append((0, 0, 0))
dSide = [[0], [2, 4], [1, 3], [2, 4], [1, 3]]
dFront = [0, 3, 4, 1, 2]
for goal in order:
    nextq = {}
    while queue:
        a, b, power = queue.popleft()
        if a == goal or b == goal:
            nextq = addQ(nextq, a, b, power+1)
            continue
        if a == 0:
            nextq = addQ(nextq, goal, b, power+2)
        if a in dSide[goal]:
            nextq = addQ(nextq, goal, b, power+3)
        if b in dSide[goal]:
            nextq = addQ(nextq, goal, a, power+3)
        if a == dFront[goal]:
            nextq = addQ(nextq, goal, b, power+4)
        if b == dFront[goal]:
            nextq = addQ(nextq, goal, a, power+4)
    for a, b in nextq:
        queue.append((a, b, nextq[(a, b)]))
print(min(list(nextq.values())))
