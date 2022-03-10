# Solved on 2022. 3. 10.
# 6198 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

N = int(input())
stack = []
count = 0
for _ in range(N):
    n = int(input())
    
    while stack and stack[-1] <= n:
        stack.pop()
    stack.append(n)
    count += len(stack) - 1
print(count)
