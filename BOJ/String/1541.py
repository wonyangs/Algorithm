# Solved on 2021. 10. 03.
# 1541 잃어버린 괄호

import sys
input = sys.stdin.readline

string = input().strip().split('-')

a = []
for s in string:
    hap = 0
    tmp = s.split('+')
    for c in tmp:
        hap += int(c)
    a.append(hap)

result = a[0]
for i in range(1, len(a)):
    result -= a[i]

print(result)
