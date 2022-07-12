# Solved on 2022. 7. 12.
# 1212 8진수 2진수

import sys
input = sys.stdin.readline

print(format(int(input().strip(), 8), 'b'))
