# Solved on 2021. 11. 29.
# 2580 스도쿠

import sys
input = sys.stdin.readline


def canPlace(arr, x, y, num):
    for i in range(9):
        if num == arr[i][y]:
            return False
    for j in range(9):
        if num == arr[x][j]:
            return False
    if x < 3:
        nx = 0
    elif x < 6:
        nx = 3
    else:
        nx = 6
    if y < 3:
        ny = 0
    elif y < 6:
        ny = 3
    else:
        ny = 6
    for i in range(3):
        for j in range(3):
            if num == arr[nx+i][ny+j]:
                return False
    return True


# 재귀
def sudoku(graph, depth):
    global end
    if end is True:
        return
    if depth >= len(blank):
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=' ')
            print()
        end = True
        return

    a, b = blank[depth]
    for n in range(1, 10):
        if canPlace(graph, a, b, n):
            graph[a][b] = n
            sudoku(graph, depth+1)
            graph[a][b] = 0


graph = [list(map(int, input().split())) for _ in range(9)]

end = False
blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

sudoku(graph, 0)
