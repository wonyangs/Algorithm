# Solved on 2021.01.09.
# 2108 통계학

# ---------------------------

from collections import Counter
import math
import sys
input = sys.stdin.readline


def modefinder(array):
    c = Counter(array)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])

    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

print(round(sum(array)/n))
print(array[math.floor(n/2)])
print(modefinder(array))
print(max(array)-min(array))
