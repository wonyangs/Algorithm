# Solved on 2022. 5. 16.
# 11721 열 개씩 끊어 출력하기

import sys
input = sys.stdin.readline

string = input().strip()

for i in range(0, len(string), 10):
    print(string[i:i+10])
