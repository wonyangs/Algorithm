import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    x, y = map(int, input().split())
    
    if len(stack) == 0:
        stack.append(x)
        stack.append(y)
        continue
    
    if stack[-1] > x:
        while len(stack) != 0 and stack[-1] > x and stack[-1] < y:
            stack.pop()
        if stack[-1] < y:
            stack.append(y)
    else:
        stack.append(x)
        stack.append(y)
    
res = 0
for i in range(0, len(stack), 2):
    res += stack[i+1] - stack[i]
print(res)
