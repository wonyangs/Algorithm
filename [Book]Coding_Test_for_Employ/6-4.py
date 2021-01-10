# Solved on 2021. 01. 09
# 6-4 두 배열의 원소 교체

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))
