# Solved on 2022. 3. 25.
# 17071 숨바꼭질 5

import sys
input = sys.stdin.readline
MAX = 500000

def bfs():
    queue = [N]
    visit = [[False] * (MAX+1) for _ in range(2)]
    visit[0][N] = True
    global K

    check, count = 0, 0
    while queue:
        if K > MAX:
            break
        if visit[check][K] : return count

        tmp = []
        check = 1 - check
        for x in queue:
            for i in (x+1, x-1, x*2):
                if 0 <= i <= MAX and not visit[check][i]:
                    visit[check][i] = True
                    tmp.append(i)
        count += 1
        K += count
        queue = tmp
    
    return -1

N, K = map(int, input().split())
print(bfs())
