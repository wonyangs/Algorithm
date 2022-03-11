# Solved on 2022. 3. 11.
# 3015 오아시스 재결합

import sys
input = sys.stdin.readline

N = int(input())
stack, count = [], 0
for _ in range(N):
    n = int(input())
    while stack and stack[-1][0] < n:
        count += stack.pop()[1]
    
    if stack and stack[-1][0] == n:
        tmp = stack.pop()
        if stack: count += 1
        stack.append((n, tmp[1]+1))
        count += tmp[1]
    else:
        if stack: count += 1
        stack.append((n, 1))
print(count)
