# Solved on 2022. 2. 10.
# 2577 숫자의 개수

from collections import defaultdict
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

res = a*b*c
dic = defaultdict(int)
while res > 0:
    dic[res%10] += 1
    res //= 10
for i in range(10):
    print(dic[i])
