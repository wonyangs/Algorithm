# Solved on 2022. 7. 30.
# 17256 달달함이 넘쳐흘러

import sys
input = sys.stdin.readline

a = [*map(int, input().split())]
c = [*map(int, input().split())]
print(c[0]-a[2], c[1]//a[1], c[2]-a[0])
