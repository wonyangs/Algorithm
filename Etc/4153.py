# Solved on 2021. 08. 29.
# 4153 직각삼각형

import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    nums = sorted(nums)

    if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
        break

    if pow(nums[0], 2) + pow(nums[1], 2) == pow(nums[2], 2):
        print("right")
    else:
        print("wrong")
