import sys
input = sys.stdin.readline

N = int(input())
stack = [int(input())]

for _ in range(N-1):
    n = int(input())
    while stack:
        if stack[-1] <= n:
            stack.pop()
        else:
            break
    stack.append(n)
print(len(stack))
