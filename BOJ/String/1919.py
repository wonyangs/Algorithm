# Solved on 2022. 3. 22.
# 1919 애너그램 만들기

from collections import Counter
import sys
input = sys.stdin.readline

a = Counter(input().strip())
b = Counter(input().strip())

res = 0
for c in a.keys():
    if c in b:
        res += abs(a[c] - b[c])
    else:
        res += a[c]
for c in b.keys():
    if c not in a:
        res += b[c]
print(res)
