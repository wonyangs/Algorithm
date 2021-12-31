# Solved on 2020.12.15
# 11866 요세푸스 문제 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(i+1 for i in range(N))

count = 0
print('<', end='')
while len(a) > 0:
    count -= 1
    count += K
    while count >= len(a):
        count -= len(a)
    print(a.pop(count), end='')
    if len(a) > 0:
        print(', ', end='')
    else:
        print('>')
