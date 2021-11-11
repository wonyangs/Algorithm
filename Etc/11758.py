# Solved on 2021. 11. 11.
# 11758 CCW

import sys
input = sys.stdin.readline

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

s = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
if s > 0:
    print(1)
elif s < 0:
    print(-1)
else:
    print(0)
