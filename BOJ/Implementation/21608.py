# Solved on 2022. 2. 24.
# 21608 상어 초등학교

import sys
input = sys.stdin.readline   

N = int(input())
graph = [[0]*N for _ in range(N)]
f_member = [[] for _ in range(N*N+1)]
member_order = []
for _ in range(N*N):
    m = [*map(int, input().split())]
    f_member[m[0]] = set(m[1:])
    member_order.append(m[0])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for num in member_order:
    MAX = -1
    metrix_list = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                continue
            
            count = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if graph[nx][ny] in f_member[num]:
                    count += 1
            if count > MAX:
                MAX = count
                metrix_list = []
                metrix_list.append((i, j))
            elif count == MAX:
                metrix_list.append((i, j))
    if len(metrix_list) == 1:
        x, y = metrix_list[0]
        graph[x][y] = num
        continue
    
    MAX = -1
    blank_list = []
    for x, y in metrix_list:
        count = 0
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 0:
                count+=1
        if count > MAX:
            MAX = count
            blank_list = []
            blank_list.append((x, y))
        elif count == MAX:
            blank_list.append((x, y))
    blank_list.sort()
    x, y = blank_list[0]
    graph[x][y] = num

res = 0
for i in range(N):
    for j in range(N):
        count = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] in f_member[graph[i][j]]:
                count += 1
        if count == 0:
            continue
        res += 10 ** (count-1)
print(res)