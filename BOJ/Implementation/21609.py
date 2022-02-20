# Solved on 2022. 2. 20.
# 21609 상어 중학교

from collections import deque
import sys
input = sys.stdin.readline   

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit = [[False] * N for _ in range(N)]
    visit[x][y] = True
    color = graph[x][y]
    group = []
    group.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visit[nx][ny] and (graph[nx][ny] == color or graph[nx][ny] == 0):
                visit[nx][ny] = True
                queue.append([nx, ny])
                group.append([nx, ny])
    return group

def count_rainbow(group):
    count = 0
    for x, y in group:
        if graph[x][y] == 0:
            count += 1
    return count

def main_block(group):
    for x, y in group:
        if graph[x][y] != 0:
            return (-x, -y)

def find_group():
    visit = set()
    groups = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in visit and graph[i][j] > 0:
                group = bfs(i, j)
                for x, y in group:
                    visit.add((x, y))
                group.sort()
                groups.append(group)
    if not len(groups):
        return -1
    
    groups.sort(key=lambda x: (-len(x), -count_rainbow(x), main_block(x)))
    if len(groups[0]) < 2:
        return -1
    
    return groups[0]


def delete_group(group):
    global point
    point += len(group) ** 2
    for x, y in group:
        graph[x][y] = -2
    
def get_row(n):
    arr = []
    for x in range(N):
        arr.append(graph[x][n])
    return arr

def set_row(arr, n):
    for x in range(N):
        graph[x][n] = arr[x]
    return arr

def down_blocks():
    for y in range(N):
        arr = get_row(y)
        arr.reverse()
        stack, res = [], []
        for n in arr:
            if n >= 0:
                res.append(n)
            elif n == -1:
                for s in stack:
                    res.append(s)
                res.append(n)
                stack = []
            elif n == -2:
                stack.append(n)
        for s in stack:
            res.append(s)
        res.reverse()
        set_row(res, y)

def rotate_graph():
    new_graph = [[0]*N for _ in range(N)]
    # y=-x축 대칭
    for i in range(N):
        for j in range(N):
            new_graph[i][j] = graph[j][i]
    # 상하 반전
    for i in range(N):
        for j in range(N):
            graph[i][j] = new_graph[N-i-1][j]

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
point = 0

while True:
    group = find_group()
    if group == -1:
        print(point)
        break
    
    delete_group(group)
    down_blocks()
    rotate_graph()
    down_blocks()
