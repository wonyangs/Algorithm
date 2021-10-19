# Solved on 2021. 10. 18.
# 1065 한수

import sys
input = sys.stdin.readline

N = int(input())

count = 0
for i in range(1, N+1):
    arr = [int(n) for n in str(i)]
    if i < 10:
        count += 1
        continue
    d = arr[1] - arr[0]
    res = True
    for j in range(len(arr)-1):
        if arr[j] != arr[j+1] - d:
            res = False
    if res:
        count += 1
print(count)
