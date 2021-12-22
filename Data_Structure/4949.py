# Solved on 2021. 12. 22.
# 4949 균형잡힌 세상

import sys
input = sys.stdin.readline

while True:
    stack = []
    balance = True
    arr = list(input().rstrip())
    if arr == ['.']:
        break
    for ch in arr:            
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0 or stack[-1] != '(':
                balance = False
            else:
                stack.pop()
        elif ch == ']':
            if len(stack) == 0 or stack[-1] != '[':
                balance = False
            else:
                stack.pop()
    if len(stack) != 0:
        balance = False
    if balance:
        print("yes")
    else:
        print("no")
