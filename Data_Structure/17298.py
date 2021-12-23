# Solved on 2021. 12. 22.
# 17298 오큰수

import sys
input = sys.stdin.readline


N = int(input())
arr = [*map(int, input().split())]

arr = arr[::-1]
tmp = []
for i in range(N):
    tmp.append((arr[i], N-i-1))
log = [-1] * (N+1)
stack = []
while tmp:
    n, i = tmp.pop()
    if len(stack) != 0:
        while True:
            if len(stack) == 0 or stack[-1][0] >= n:
                break
            else:
                num, index = stack.pop()
                log[index] = n
    stack.append((n, i))
for n in log[:N]:
    print(n, end=' ')
print()
