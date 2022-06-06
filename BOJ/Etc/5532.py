# Solved on 2022. 6. 7.
# 5532 방학 숙제

L = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

aa = a // c
bb = b // d
if a % c != 0:
    aa += 1
if b % d != 0:
    bb += 1

print(L - max(aa, bb))