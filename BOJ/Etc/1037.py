# Solved on 2021. 11. 07.
# 1037 약수

import sys
input = sys.stdin.readline

n = int(input())
divs = list(map(int, input().split()))
divs.sort()
print(divs[0] * divs[-1])
