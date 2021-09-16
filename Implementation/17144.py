# Solved on 2021. 09. 16.
# 17144 미세먼지 안녕!

import sys
input = sys.stdin.readline


# 조건 입력
R, C, T = map(int, input().split())

graph = []

for _ in range(R):
    graph.append(list(map(int, input().split())))


# 해당 좌표 먼지 확산
def dustDiffusion(x, y, amount):
    count = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        elif graph[nx][ny] == -1:
            continue
        else:
            graph[nx][ny] += amount // 5
            count += 1
    graph[x][y] -= (amount // 5) * count


# 현재 먼지들 좌표 반환
def findDust():
    queue = []

    for i in range(R):
        for j in range(C):
            if graph[i][j] >= 5:
                queue.append([i, j, graph[i][j]])

    return queue


# 공기청정기 좌표 반환
def findCleaner():
    for i in range(R):
        if graph[i][0] == -1:
            return i


# 위쪽 공기청정기 작동
def upperCleaner():
    cleaner = findCleaner()
    tmp1 = 0
    for i in range(1, C):
        tmp2 = graph[cleaner][i]
        graph[cleaner][i] = tmp1
        tmp1 = tmp2
    for i in range(cleaner-1, -1, -1):
        tmp2 = graph[i][C-1]
        graph[i][C-1] = tmp1
        tmp1 = tmp2
    for i in range(C-2, -1, -1):
        tmp2 = graph[0][i]
        graph[0][i] = tmp1
        tmp1 = tmp2
    for i in range(1, cleaner):
        tmp2 = graph[i][0]
        graph[i][0] = tmp1
        tmp1 = tmp2


# 아래쪽 공기청정기 작동
def lowerCleaner():
    cleaner = findCleaner() + 1
    tmp1 = 0
    for i in range(1, C):
        tmp2 = graph[cleaner][i]
        graph[cleaner][i] = tmp1
        tmp1 = tmp2
    for i in range(cleaner+1, R):
        tmp2 = graph[i][C-1]
        graph[i][C-1] = tmp1
        tmp1 = tmp2
    for i in range(C-2, -1, -1):
        tmp2 = graph[R-1][i]
        graph[R-1][i] = tmp1
        tmp1 = tmp2
    for i in range(R-2, cleaner, -1):
        tmp2 = graph[i][0]
        graph[i][0] = tmp1
        tmp1 = tmp2


# 1초 실행
def simulateOneSecond():
    dust = findDust()
    dust.reverse()

    while dust:
        x, y, amount = dust.pop()
        dustDiffusion(x, y, amount)
    upperCleaner()
    lowerCleaner()


for _ in range(T):
    simulateOneSecond()

hap = 0
for i in range(R):
    hap += sum(graph[i])

print(hap+2)
