# Solved on 2022. 6. 1.
# 4101 크냐?

import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break;
    if a > b:
        print("Yes")
    else:
        print("No")
