# Solved on 2021. 09. 24.
# 9663 N-Queen

import sys
input = sys.stdin.readline

N = int(input())
a = [False] * N
b = [False] * (2*N-1)
c = [False] * (2*N-1)


def dfs(i):
    global result

    if i == N:
        result += 1
        return

    for j in range(N):
        if not (a[j] or b[i+j] or c[i-j+N-1]):
            a[j] = b[i+j] = c[i-j+N-1] = True
            dfs(i+1)
            a[j] = b[i+j] = c[i-j+N-1] = False


result = 0
dfs(0)
print(result)
