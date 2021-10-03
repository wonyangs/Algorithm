# Solved on 2021. 10. 04.
# 9935 문자열 폭발

import sys
input = sys.stdin.readline

string = input().strip()
stack = []
bomb = input().strip()

for c in string:
    stack.append(c)
    if c == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
