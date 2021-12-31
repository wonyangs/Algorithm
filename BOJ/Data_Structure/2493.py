# Solved on 2021. 11. 07.
# 2493 탑

import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
catch = [0] * N
stack = []

stack.append((tower[0], 1))
for i in range(1, N):
    while stack and stack[-1][0] < tower[i]:
        length, num = stack.pop()
        if stack:
            catch[num-1] = stack[-1][1]
    stack.append((tower[i], i+1))

while stack:
    length, num = stack.pop()
    if stack:
        catch[num-1] = stack[-1][1]

for n in catch:
    print(n, end=' ')
print()
