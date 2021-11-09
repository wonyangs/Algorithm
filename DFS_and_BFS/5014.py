# Solved on 2021. 11. 09.
# 5014 스타트링크

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((S, 0))

    clear = False
    visit = set()
    while queue:
        now, count = queue.popleft()
        if now in visit:
            continue
        else:
            visit.add(now)

        if now == G:
            clear = True
            print(count)
            break

        if U != 0 and now + U <= F:
            queue.append((now + U, count+1))
        if D != 0 and now - D > 0:
            queue.append((now - D, count+1))
    if clear is False:
        print('use the stairs')


F, S, G, U, D = map(int, input().split())
bfs()
