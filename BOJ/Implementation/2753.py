# Solved on 2021.08.28
# 2753 윤년

import sys
input = sys.stdin.readline

year = int(input())

if year % 400 == 0:
    print(1)
elif year % 4 == 0 and year % 100 != 0:
    print(1)
else:
    print(0)
