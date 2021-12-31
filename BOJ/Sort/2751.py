# Solved on 2020.12.13
# 2751 수 정렬하기 2

from sys import stdin, stdout

n = int(input())
L = []

for i in range(n):
    L.append(int(stdin.readline()))

for i in sorted(L):
    stdout.write(str(i)+'\n')
