# Solved on 2022. 3. 12.
# 10799 쇠막대기

import sys
input = sys.stdin.readline

string = input().strip()
count, res = 0, 0
laser = False
for c in string:
    if c == '(':
        count += 1
        laser = True
    else:
        count -= 1
        if laser:
            res += count
            laser = False
        else:
            res += 1
print(res)
