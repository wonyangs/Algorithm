# Solved on 2022. 7. 5.
# 1032 명령 프롬프트

import sys
input = sys.stdin.readline

for n in [*zip(*[input().strip() for _ in range(int(input()))])]:
    if len(set(n)) == 1:
        print(n[0], end="")
    else:
        print("?", end="")
