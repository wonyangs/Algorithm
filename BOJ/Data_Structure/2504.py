# Solved on 2022. 3. 12.
# 2504 괄호의 값

import sys
input = sys.stdin.readline

string = input().strip()
count, res = 0, 0
stack, num = [], []
for ch in string:
    if ch == '(':
        stack.append(ch)
        num.append(0)
    elif ch == '[':
        stack.append(ch)
        num.append(0)
    elif ch == ')':
        if not stack or stack[-1] != '(':
            print(0)
            sys.exit(0)
        stack.pop()
        t = num.pop()
        if t == 0:
            t = 1
        if len(num) != 0:
            num[-1] += t * 2
        else:
            res += t * 2
    else:
        if not stack or stack[-1] != '[':
            print(0)
            sys.exit(0)
        stack.pop()
        t = num.pop()
        if t == 0:
            t = 1
        if len(num) != 0:
            num[-1] += t * 3
        else:
            res += t * 3

if stack:
    print(0)
else:
    print(res)
