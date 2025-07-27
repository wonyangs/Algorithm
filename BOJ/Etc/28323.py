import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d0 = d1 = 0
for x in a:
    if x % 2 == 0:
        if d1 + 1 > d0:
            d0 = d1 + 1
    else:
        if d0 + 1 > d1:
            d1 = d0 + 1
print(d0 if d0 > d1 else d1)
