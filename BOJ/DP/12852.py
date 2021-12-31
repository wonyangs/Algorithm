# Solved on 2021. 10. 04.
# 12852 1로 만들기 2

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dp = [INF] * (n+1)


def bfs(start):
    queue = deque()
    queue.append((start, []))
    dp[start] = 0

    while queue:
        now, arr = queue.popleft()
        v = len(arr)
        if now == 1:
            result = arr
            return result+[1]

        if now % 2 == 0 and dp[now // 2] > v+1:
            dp[now // 2] = v+1
            queue.append((now // 2, arr+[now]))
        if now % 3 == 0 and dp[now // 3] > v+1:
            dp[now // 3] = v+1
            queue.append((now // 3, arr+[now]))
        if now > 1 and dp[now - 1] > v+1:
            dp[now - 1] = v+1
            queue.append((now - 1, arr+[now]))

    return result+[1]


arr = bfs(n)
print(dp[1])
for n in arr:
    print(n, end=' ')
