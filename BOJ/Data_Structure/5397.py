# Solved on 2022. 3. 5.
# 5397 키로거

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    String = input().strip()
    left, right = [], deque()
    for ch in String:
        if ch == '<':
            if left:
                right.appendleft(left.pop())
        elif ch == '>':
            if right:
                left.append(right.popleft())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)
    print(''.join(left) + ''.join(right))
