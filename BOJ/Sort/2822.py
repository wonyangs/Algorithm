# Solved on 2022. 5. 15.
# 2822 점수 계산

import sys
input = sys.stdin.readline

arr = []
for i in range(1, 9):
    arr.append((int(input()), i))

arr.sort()
arr.reverse()
res = []
point = 0
for i in range(5):
    point += arr[i][0]
    res.append(arr[i][1])
res.sort()
print(point)
print(*res)
