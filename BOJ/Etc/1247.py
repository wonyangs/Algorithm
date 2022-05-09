# Solved on 2022. 5. 9.
# 1247 부호

import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    hap = 0
    for _ in range(N):
        hap += int(input())
    
    if hap > 0:
        print("+")
    elif hap < 0:
        print("-")
    else:
        print(0)
