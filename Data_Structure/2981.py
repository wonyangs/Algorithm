# Solved on 2021. 12. 22.
# 2981 검문

import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
