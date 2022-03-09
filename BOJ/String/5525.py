# Solved on 2022. 3. 9.
# 5525 IOIOI

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
string = input().strip()
i, info = 0, []
while i < len(string):
    p_cnt = 0
    while string[i] == 'I' and i+2 < len(string):
        if string[i+1] == 'O' and string[i+2] == 'I':
            p_cnt += 1
            i += 2
        else:
            break
    if p_cnt != 0:
        info.append(p_cnt)
    i += 1

count = 0
for n in info:
    if n - N + 1 > 0:
        count += n - N + 1
print(count)
