# Solved on 2021. 08. 29.
# 2579 계단 오르기

import sys
input = sys.stdin.readline

x = int(input())

d = [0] * 301
array = [0] * 301

for i in range(x):
    array[i] = int(input())
    
d[0] = array[0]
d[1] = array[1] + array[0]
d[2] = max(array[1], array[0]) + array[2]

for i in range(3, x):
    d[i] = max(array[i-1] + d[i-3], d[i-2]) + array[i]
    
print(d[x-1])
