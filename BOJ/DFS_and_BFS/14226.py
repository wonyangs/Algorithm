# Solved on 2021. 09. 27.
# 14226 이모티콘

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
maxNum = 1000

S = int(input())
dp = [INF] * (maxNum + 1)


def bfs(start):
    queue = deque()
    queue.append((start, 0, 0))
    dp[start] = 0

    while queue:
        now, clip, count = queue.popleft()

        # 클립보드에 복사
        if now != clip:
            queue.append((now, now, count + 1))
        # 붙여넣기
        if clip != 0 and now + clip <= maxNum:
            if dp[now + clip] > count + 1:
                dp[now + clip] = count + 1
            queue.append((now + clip, clip, count + 1))
        # 하나 삭제
        if now - 1 > 0 and dp[now-1] > count + 1:
            dp[now-1] = count + 1
            queue.append((now-1, clip, count + 1))


bfs(1)
print(dp[S])


