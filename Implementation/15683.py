# Solved on 2021. 10. 08.
# 15683 감시

from itertools import product
import sys
input = sys.stdin.readline


def upside(x, y):
    upside = set()
    for i in range(x, -1, -1):
        if graph[i][y] == 6:
            break
        if graph[i][y] == 0:
            upside.add((i, y))
    return upside


def downside(x, y):
    downside = set()
    for i in range(x, N):
        if graph[i][y] == 6:
            break
        if graph[i][y] == 0:
            downside.add((i, y))
    return downside


def leftside(x, y):
    leftside = set()
    for i in range(y, -1, -1):
        if graph[x][i] == 6:
            break
        if graph[x][i] == 0:
            leftside.add((x, i))
    return leftside


def rightside(x, y):
    rightside = set()
    for i in range(y, M):
        if graph[x][i] == 6:
            break
        if graph[x][i] == 0:
            rightside.add((x, i))
    return rightside


def cctv(typ, x, y):
    up = upside(x, y)
    down = downside(x, y)
    left = leftside(x, y)
    right = rightside(x, y)

    if typ == 1:
        arr = []
        # 위쪽
        arr.append(up)
        # 아래쪽
        arr.append(down)
        # 오른쪽
        arr.append(right)
        # 왼쪽
        arr.append(left)
        return arr
    elif typ == 2:
        arr = []
        # 왼쪽 오른쪽
        arr.append(set.union(left, right))
        # 위쪽 아래쪽
        arr.append(set.union(up, down))
        return arr
    elif typ == 3:
        arr = []
        # 상좌
        arr.append(set.union(up, left))
        # 좌하
        arr.append(set.union(left, down))
        # 하우
        arr.append(set.union(down, right))
        # 우상
        arr.append(set.union(up, right))
        return arr
    elif typ == 4:
        arr = []
        # 하 제외
        arr.append(set.union(left, right, up))
        # 좌 제외
        arr.append(set.union(down, right, up))
        # 상 제외
        arr.append(set.union(left, right, down))
        # 우 제외
        arr.append(set.union(left, down, up))
        return arr
    elif typ == 5:
        arr = []
        arr.append(set.union(left, right, down, up))
        return arr
    else:
        print('type error')


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

arr = []
items = []
safty = 0
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:
            arr.append(cctv(graph[i][j], i, j))
            if graph[i][j] == 2:
                items.append(list(i for i in range(2)))
            elif graph[i][j] == 5:
                items.append([0])
            else:
                items.append(list(i for i in range(4)))
        elif graph[i][j] == 0:
            safty += 1

p = list(product(*items))
result = []
for i in range(len(p)):
    s = set()
    for j in range(len(arr)):
        s = set.union(s, arr[j][p[i][j]])
    result.append(len(s))
print(safty - max(result))
