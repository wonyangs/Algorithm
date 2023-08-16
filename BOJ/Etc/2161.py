from collections import deque
N = int(input())
stack = deque([i for i in range(1, N + 1)])

while len(stack) != 1:
    b = stack.popleft()
    stack.rotate(-1)
    print(b, sep=' ')
print(stack[0])
