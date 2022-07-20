# Solved on 2022. 7. 20.
# 10768 특별한 날

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

if a < 2:
    print("Before")
elif a > 2:
    print("After")
else:
    if b < 18:
        print("Before")
    elif b > 18:
        print("After")
    else:
        print("Special")

