# Solved on 2022. 06. 16.
# 9328 열쇠

from collections import deque
import sys
input = sys.stdin.readline


def can_move(ch, keys):
    if ch == '#':
        return False
    elif ch == '.' or ch == '$':
        return True
    elif ord('a') <= ord(ch) <= ord('z'):
        return True
    else:
        for key in keys:
            if ord(ch) + ord('a') - ord('A') == ord(key):
                return True
        return False


def bfs(height, width, keys):
    queue = deque()
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while True:
        visit = [[False] * width for _ in range(height)]
        count = 0
        start_point = set()
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                    if can_move(graph[i][j], keys):
                        if ord('a') <= ord(graph[i][j]) <= ord('z') and graph[i][j] not in keys:
                            keys.add(graph[i][j])
                        start_point.add((i, j))
        for x, y in start_point:
            if graph[x][y] == '$':
                count += 1
            queue.append((x, y))
            visit[x][y] = True
        find_key = False

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= height or ny >= width:
                    continue
                if not visit[nx][ny] and can_move(graph[nx][ny], keys):
                    if graph[nx][ny] == '$':
                        count += 1
                    if ord('a') <= ord(graph[nx][ny]) <= ord('z') and graph[nx][ny] not in keys:
                        keys.add(graph[nx][ny])
                        find_key = True
                    queue.append((nx, ny))
                    visit[nx][ny] = True
        if not find_key:
            return count


T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    graph = [[*map(str, input().strip())] for _ in range(h)]
    key_info = input().strip()
    if key_info == '0':
        keys = set()
    else:
        keys = set([*map(str, key_info)])

    print(bfs(h, w, keys))
