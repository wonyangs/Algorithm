# Solved on 2021. 11. 25.
# 12100 2048 (Easy)

import copy
import sys
input = sys.stdin.readline

# 이동 가능 여부 확인
def canMoveSide(graph):
    for i in range(N):
        for j in range(N-1):
            if graph[i][j] == 0:
                continue
            if graph[i][j] == graph[i][j+1]:
                return True
    return False


def canMoveUpdown(graph):
    for j in range(N):
        for i in range(N-1):
            if graph[i][j] == 0:
                continue
            if graph[i][j] == graph[i+1][j]:
                return True
    return False


def canMoveLeft(graph):
    for i in range(N):
        findNum = False
        for j in range(N):
            if graph[i][j] == 0:
                findNum = True
            else:
                if findNum:
                    return True
    return False


def canMoveRight(graph):
    for i in range(N):
        findNum = False
        for j in range(N-1, -1, -1):
            if graph[i][j] == 0:
                findNum = True
            else:
                if findNum:
                    return True
    return False


def canMoveUpper(graph):
    for j in range(N):
        findNum = False
        for i in range(N):
            if graph[i][j] == 0:
                findNum = True
            else:
                if findNum:
                    return True
    return False


def canMoveDown(graph):
    for j in range(N):
        findNum = False
        for i in range(N-1, -1, -1):
            if graph[i][j] == 0:
                findNum = True
            else:
                if findNum:
                    return True
    return False


# 블럭 합치기
def addBlocks(blocks):
    arr = []
    for n in blocks:
        if n != 0:
            arr.append(n)
    for i in range(len(arr)-1):
        if arr[i] == 0:
            continue
        if arr[i] == arr[i+1]:
            arr[i] *= 2
            arr[i+1] = 0
    tmp = []
    for n in arr:
        if n != 0:
            tmp.append(n)
    leng = N - len(tmp)
    for _ in range(leng):
        tmp.append(0)
    return tmp


# 이동
def moveLeft(graph):
    for i in range(N):
        graph[i] = addBlocks(graph[i])
    return graph


def moveRight(graph):
    for i in range(N):
        arr = addBlocks(list(reversed(graph[i])))
        arr.reverse()
        graph[i] = arr
    return graph


def moveUpper(graph):
    for j in range(N):
        arr = []
        for i in range(N):
            arr.append(graph[i][j])
        arr = addBlocks(arr)
        for i in range(N):
            graph[i][j] = arr[i]
    return graph


def moveDown(graph):
    for j in range(N):
        arr = []
        for i in range(N):
            arr.append(graph[i][j])
        arr.reverse()
        arr = addBlocks(arr)
        arr.reverse()
        for i in range(N):
            graph[i][j] = arr[i]
    return graph


# 그래프 최대값 반환
def maxNumber(graph):
    MAX = 0
    for i in range(N):
        for j in range(N):
            MAX = max(MAX, graph[i][j])
    return MAX


# 재귀
def playGame(graph, depth):
    global res
    if depth >= 5:
        res = max(res, maxNumber(graph))
        return
    tmp = copy.deepcopy(graph)
            
    if canMoveSide(graph) or canMoveLeft(graph):
        playGame(moveLeft(graph), depth+1)
        graph = copy.deepcopy(tmp)
    if canMoveSide(graph) or canMoveRight(graph):
        playGame(moveRight(graph), depth+1)
        graph = copy.deepcopy(tmp)
    if canMoveUpdown(graph) or canMoveUpper(graph):
        playGame(moveUpper(graph), depth+1)
        graph = copy.deepcopy(tmp)
    if canMoveUpdown(graph) or canMoveDown(graph):
        playGame(moveDown(graph), depth+1)
        graph = copy.deepcopy(tmp)
    res = max(res, maxNumber(graph))
    return


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
res = 0
playGame(graph, 0)
print(res)