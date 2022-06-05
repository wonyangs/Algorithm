# Solved on 2022. 6. 6.
# 10808 알파벳 개수

import sys

arr = [0] * (ord('z')-ord('a') + 1)
for i in input().strip():
    arr[ord(i) - ord('a')] += 1
print(*arr)