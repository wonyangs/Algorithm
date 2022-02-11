# Solved on 2022. 2. 11.
# 14936 엘리베이터 장난

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def dfs(n, time):
    nums.add(n)
    if time <= 0 or (n, time) in log:
        return
    log.add((n, time))
    if time >= N:
        dfs(n^every_button, time-N)
    if time >= N//2:
        dfs(n^even_button, time-N//2)
    if time >= N - N//2:
        dfs(n^odd_button, time-(N-N//2))
    if time >= (N-1)//3 + 1:
        dfs(n^three_button, time-((N-1)//3+1))


N, M = map(int, input().split())
every_button = 2**N - 1
even_button = int('0'+'10'*(N//2), 2)
odd_button = int('10'*((N-1)//2)+'1', 2)
three_button = int('100'*((N-1)//3)+'1', 2)
nums, log = set(), set()
dfs(0, M)
print(len(nums))
