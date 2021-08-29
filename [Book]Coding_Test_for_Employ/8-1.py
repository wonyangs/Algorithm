# Solved on 2021. 08. 29.
# 8-1 1로 만들기

import sys
input = sys.stdin.readline

d = [0] * 30001

num = int(input())

for i in range(2, num+1):
    d[i] = d[i-1] + 1
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[num])
