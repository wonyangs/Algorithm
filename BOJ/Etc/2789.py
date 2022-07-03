# Solved on 2022. 7. 4.
# 2789 유학 금지

import sys
input = sys.stdin.readline

arr = input().strip()
for n in arr:
    if n not in "CAMBRIDGE":
        print(n, end="")
