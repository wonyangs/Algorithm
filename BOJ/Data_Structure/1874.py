# Solved on 2021. 12. 22.
# 1874 스택 수열

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
count = 0
i = 1
stack = []
log = []
while True:
    if i > N and len(stack) == 0:
        break
    if len(stack) == 0 or stack[-1] != arr[count]:
        if i > N:
            break
        stack.append(i)
        log.append('+')
        i += 1
    else:
        stack.pop()
        count += 1
        log.append('-')
if len(stack) == 0:
    for n in log:
        print(n)
else:
    print('NO')
