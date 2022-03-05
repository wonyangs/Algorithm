# Solved on 2022. 3. 5.
# 1406 에디터

import sys
input = sys.stdin.readline

string = input().strip()
N = int(input())
left, right = [*string], []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[1])
print(''.join(left)+''.join(reversed(right)))
