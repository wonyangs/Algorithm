# Solved on 2022. 7. 9.
# 1076 저항

import sys
input = sys.stdin.readline

info = {"black": 0, "brown": 1, "red": 2,
        "orange": 3, "yellow": 4, "green": 5,
        "blue": 6, "violet": 7,
        "grey": 8, "white": 9}

res = 0
res += (info[input().strip()] * 10)
res += info[input().strip()]
res *= (10 ** info[input().strip()])
print(res)
