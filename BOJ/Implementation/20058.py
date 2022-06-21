# Solved on 2022. 6. 21.
# 20058 마법사 상어와 파이어스톰

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, visit):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= 2 ** N or ny >= 2 ** N:
                continue
            if visit[nx][ny] == -1 and graph[nx][ny] != 0:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
                count += 1
    return count


def biggest_ice():
    visit = [[-1] * 2**N for _ in range(2**N)]
    MAX = 0
    for x in range(2**N):
        for y in range(2**N):
            if visit[x][y] == -1 and graph[x][y] != 0:
                MAX = max(MAX, bfs(x, y, visit))
    return MAX


def total_ice():
    result = 0
    for x in range(2**N):
        for y in range(2**N):
            result += graph[x][y]
    return result


def break_ice():
    check_ice = set()
    for x in range(2**N):
        for y in range(2**N):
            count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= 2**N or ny >= 2**N:
                    continue
                if graph[nx][ny] != 0:
                    count += 1
            if count < 3 and graph[x][y] > 0:
                check_ice.add((x, y))
    for x, y in check_ice:

        graph[x][y] -= 1


def turn_graph(lv):
    for i in range(0, 2**N, 2**lv):
        for j in range(0, 2**N, 2**lv):
            tmp_graph = [[0] * 2 ** lv for _ in range(2 ** lv)]
            for x in range(2**lv):
                for y in range(2**lv):
                    tmp_graph[x][y] = graph[i+x][j+y]
            tmp_graph = list(zip(*tmp_graph[::-1]))
            for x in range(2 ** lv):
                for y in range(2 ** lv):
                    graph[i + x][j + y] = tmp_graph[x][y]


N, Q = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(2**N)]
level = [*map(int, input().split())]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for lv in level:
    turn_graph(lv)
    break_ice()
print(total_ice())
print(biggest_ice())
