# Solved on 2022. 5. 19.
# 10988 팰린드롬인지 확인하기

import sys
input = sys.stdin.readline

string = input().strip()
print(1 if string == string[::-1] else 0)
