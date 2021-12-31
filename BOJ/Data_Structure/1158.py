# Solved on 2021. 11. 07.
# 1158 요세푸스 문제

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

ans = []
res = 0
for i in range(N):
    res += K - 1
    res %= (N-i)
    n = arr.pop(res)
    ans.append(n)

print('<', end='')
for i in range(N-1):
    print(ans[i], end=', ')
print(ans[-1], end='>')
print()
