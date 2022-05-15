# Solved on 2022. 5. 15.
# E. 배스킨라빈스~N~귀엽고~깜찍하게~

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
print("Can win"if 0<(N-1)%(M+1)<=M else"Can't win")