# Solved on 2021. 08. 29.
# 8-3 바닥 공사

import sys
input = sys.stdin.readline

x = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, x+1):
    d[i] = (d[i-2] * 2 + d[i-1]) % 796796
    
print(d[x])
