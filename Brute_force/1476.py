# Solved on 2021. 10. 17.
# 1476 날짜 계산

import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

a = b = c = i = 0
while True:
    i += 1
    a += 1
    b += 1
    c += 1
    
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1
        
    if a == E and b == S and c == M:
        print(i)
        break
