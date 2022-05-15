# Solved on 2022. 5. 15.
# A. 두~~부 두부 두부

import sys
input = sys.stdin.readline


N,M,K=map(int,input().split())
res=(M+K-3)%N
print(res if res!=0 else N)