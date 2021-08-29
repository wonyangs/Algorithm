# Solved on 2021. 08. 29.
# 8-2 개미 전사

import sys
input = sys.stdin.readline

x = int(input())

arr = list(map(int, input().split()))

d = [0] * (x+1)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, x):
    d[i] = max(d[i-1], d[i-2]+arr[i])
    
print(d[x-1])
