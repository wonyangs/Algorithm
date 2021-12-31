# Solved on 2021. 10. 29.
# 6603 로또

from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break

    com = list(combinations(nums[1:], 6))
    for arr in com:
        for i in arr:
            print(i, end=' ')
        print()
    print()
