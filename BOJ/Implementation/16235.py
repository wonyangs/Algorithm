# Solved on 2022. 1. 31.
# 16235 나무 재테크

import sys
input = sys.stdin.readline


def ss_season():
    for i in range(N):
        for j in range(N):
            trees = graph[i][j]
            if len(trees) == 0:
                continue
            trees.sort()
            food = 0
            dead_tree = -1
            for k in range(len(trees)):
                if ground[i][j] >= trees[k]:
                    ground[i][j] -= trees[k]
                    trees[k] += 1
                else:
                    if dead_tree == -1:
                        dead_tree = k
                    food += trees[k] // 2
            if dead_tree != -1:
                graph[i][j] = trees[:dead_tree]
            ground[i][j] += food


def fw_season():
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(N):
        for j in range(N):
            trees = graph[i][j]
            for tree in trees:
                if tree % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue
                        graph[nx][ny].append(1)
            
            ground[i][j] += A[i][j]


def count_tree():
    count = 0
    for i in range(N):
        for j in range(N):
            count += len(graph[i][j])
    return count


N, M, K = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
graph = [[[] for _ in range(N)] for _ in range(N)]
ground = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x-1][y-1].append(z)
for _ in range(K):
    ss_season()
    fw_season()
print(count_tree())
