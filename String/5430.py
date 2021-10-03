# Solved on 2021. 10. 03.
# 5430 AC

from collections import deque
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    func = list(input().strip())
    n = int(input())
    tmp = input().strip().strip('[]').split(',')
    queue = deque()
    err = False
    reverse = False

    for c in tmp:
        if c == '':
            continue
        queue.append(c)

    for f in func:
        if f == 'R':
            if reverse is False:
                reverse = True
            else:
                reverse = False
        elif f == 'D':
            if len(queue) == 0:
                print('error')
                err = True
                break
            else:
                if reverse is True:
                    queue.pop()
                else:
                    queue.popleft()
    if err is False:
        if reverse is True:
            queue.reverse()

        print("[" + ",".join(queue) + "]")
