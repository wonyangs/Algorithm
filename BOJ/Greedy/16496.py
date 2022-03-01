# Solved on 2022. 3. 1.
# 16496 큰 수 만들기

import sys
input = sys.stdin.readline

N = int(input())
numbers = [*map(int, input().split())]
numbers.sort(key=lambda x: str(x)*9, reverse=True)
print(str(int(''.join([*map(str, numbers)]))))
