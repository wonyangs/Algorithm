# Solved on 2020.12.14
# 9012 괄호

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = input()
    stack = 0
    for j in range(len(a)):
        if a[j] == '(':
            stack += 1
        elif a[j] == ')':
            stack -= 1
        else:
            continue
        if(stack < 0):
            break
    if stack == 0:
        print('YES')
    else:
        print('NO')
