# Solved on 2021. 10. 10.
# 1107 리모컨

import sys
input = sys.stdin.readline

now = 100
N = 500000

ch = int(input())
m = int(input())
if m == 0:
    breakBtns = set()
else:
    breakBtns = set(map(int, input().split()))

MIN = N
MINi = N

for i in range(2*N+1):
    tmp = i
    cani = True
    for j in range(len(str(i))):
        if int(str(i)[j]) in breakBtns:
            cani = False
            break
    if cani and abs(ch - i) < MIN:
        MIN = abs(ch - i)
        MINi = i

print(min(abs(now - ch), len(str(MINi))+MIN))
