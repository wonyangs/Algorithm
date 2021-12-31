# Solved on 2021. 12. 30.
# 2110 공유기 설치

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start, end = 1, house[-1] - house[0]
res = 0

while start <= end:
    now, count = house[0], 1
    mid = (end+start) // 2
    for n in house:
        if n >= now + mid:
            count += 1
            now = n
    if count < C:
        end = mid - 1
    else:
        start = mid + 1
        res = mid
        
print(res)
