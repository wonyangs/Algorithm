# Solved on 2022. 2. 10.
# 17822 원판 돌리기

from collections import deque
import sys
input = sys.stdin.readline


def same_number():
    change = False
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    same = set()
    for i in range(1, N+1):
        for j in range(-1, M):
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if ni < 1 or nj < -1 or ni >= N+1 or nj >= M:
                    continue
                if plates[i][j] != 0 and plates[i][j] == plates[ni][nj]:
                    same.add((i, j))
                    change = True
    for i, j in same:
        plates[i][j] = 0
    return change


def avg_number():
    hap, count = 0, 0
    for i in range(1, N+1):
        for j in range(0, M):
            if plates[i][j] != 0:
                hap += plates[i][j]
                count += 1
    if count == 0:
        return
    avg = hap / count
    for i in range(1, N+1):
        for j in range(0, M):
            if plates[i][j] != 0:
                if plates[i][j] < avg:
                    plates[i][j] += 1
                elif plates[i][j] > avg:
                    plates[i][j] -= 1


N, M, T = map(int, input().split())
plates = [[]]
for _ in range(N):
    plates.append(deque([*map(int, input().split())]))
for _ in range(T):
    x, d, k = map(int, input().split())
    if d == 1: k *= -1
    for i in range(x, N+1, x):
        plates[i].rotate(k)
    if not same_number():
        avg_number()
res = 0
for plate in plates:
    res += sum(plate)
print(res)
