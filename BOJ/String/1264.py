# Solved on 2022. 6. 24.
# 1264 모음의 개수

import sys
input = sys.stdin.readline

while True:
    string = input().strip()
    if string == "#":
        break
    
    count = 0
    for c in string:
        if c in "aeiouAEIOU":
            count += 1
    print(count)
