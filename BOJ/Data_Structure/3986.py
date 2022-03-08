# Solved on 2022. 3. 8.
# 3986 좋은 단어

import sys
input = sys.stdin.readline

N = int(input())
count = 0
for _ in range(N):
    string = input().strip()
    if len(string) % 2 == 1:
        continue
    
    stack = []
    for ch in string:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
    if not stack:
        count += 1
print(count)
