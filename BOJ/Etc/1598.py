# Solved on 2022. 7. 11.
# 1598 꼬리를 무는 숫자 나열

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print(abs((a - 1) // 4 - (b - 1) // 4) + abs((a - 1) % 4 - (b - 1) % 4))
