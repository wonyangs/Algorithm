# Solved on 2021. 10. 31.
# 14719 빗물

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
graphInfo = list(map(int, input().split()))

graph = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if graphInfo[j] >= H-i:
            graph[i][j] = 1

count = 0
for i in range(H-1, -1, -1):
    start = -1
    for j in range(W):
        if graph[i][j] == 1:
            if start == -1:
                start = j
            else:
                end = j
                for k in range(start+1, end):
                    count += 1
                start = end

print(count)
