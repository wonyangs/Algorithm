# Solved on 2022. 3. 24.
# 18808 스티커 붙이기

from collections import deque
import sys
input = sys.stdin.readline

def match_stic(i, j, R, C, stic):
    for x in range(R):
        for y in range(C):
            if stic[x][y] == 1 and graph[x+i][y+j] == 1:
                return 0
    
    count = 0
    for x in range(R):
        for y in range(C):
            if stic[x][y] == 1:
                graph[x+i][y+j] = 1
                count += 1
    return count

N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
res = 0
for _ in range(K):
    R, C = map(int, input().split())
    stic = [[*map(int, input().split())] for _ in range(R)]
    find = 0
    for _ in range(4):
        for i in range(N-R+1):
            for j in range(M-C+1):
                if find == 0:
                    find = match_stic(i, j, R, C, stic)
        
        if find != 0: break
        stic = list(zip(*stic[::-1]))
        R, C = C, R
    res += find

print(res)
