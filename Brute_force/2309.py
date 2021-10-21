# Solved on 2021. 10. 21.
# 2309 일곱 난쟁이

from itertools import combinations
import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input()))

hap = sum(arr) - 100
com = combinations(arr, 2)

for a, b in com:
    if hap == a + b:
        arr.remove(a)
        arr.remove(b)
        break
arr.sort()
for i in arr:
    print(i)
