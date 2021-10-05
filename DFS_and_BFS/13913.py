# Solved on 2021. 10. 05.
# 13913 숨바꼭질 4

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
maxNum = 100001

dp = [maxNum] * maxNum
move = [0] * maxNum


def bfs(start, end):
    queue = deque()
    queue.append(start)
    dp[start] = 0
    move[start] = start

    while queue:
        now = queue.popleft()
        if now == end:
            print(dp[k])
            ans = []
            while now != start:
                ans.append(now)
                now = move[now]
            ans.append(start)
            ans.reverse()
            for n in ans:
                print(n, end=' ')
            break

        for NEXT in (now-1, now+1, now*2):
            if 0 <= NEXT < maxNum and dp[NEXT] == maxNum:
                dp[NEXT] = dp[now] + 1
                move[NEXT] = now
                queue.append(NEXT)


if k < n:
    print(n - k)
    for i in range(n, k-1, -1):
        print(i, end=' ')
else:
    bfs(n, k)
