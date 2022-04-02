# Solved on 2022. 4. 2.
# 10825 국영수

import sys
input = sys.stdin.readline

for a in[*zip(*sorted([[*input().split()]for _ in range(int(input()))],key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0])))][0]:print(a)