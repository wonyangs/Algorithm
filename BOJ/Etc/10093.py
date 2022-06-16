# Solved on 2022. 6. 16.
# 10093 숫자

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a < b:
    arr = [i for i in range(a+1, b)]
else:
    arr = [i for i in range(b+1, a)]
print(len(arr))
print(*arr)
