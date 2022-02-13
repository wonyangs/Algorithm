# Solved on 2022. 2. 13.
# 2839 설탕 배달

import sys
input = sys.stdin.readline


N = int(input())
for i in range(N//3+1):
    if (N-3*i) % 5 == 0:
        print((N-3*i) // 5 + i)
        sys.exit(0)
print(-1)
