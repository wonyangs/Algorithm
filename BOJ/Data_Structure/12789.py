# Solved on 2022. 12. 17.
# 12789 도키도키 간식드리미

import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]

stack = []
count = 1
for num in arr:
    if num == count:
        count += 1
    else:
        stack.append(num)
    while stack and stack[-1] == count:
        count += 1
        stack.pop()
print("Nice" if not stack else "Sad")

