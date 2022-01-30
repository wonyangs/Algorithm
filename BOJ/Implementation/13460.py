# Solved on 2022. 1. 30.
# 13460 구슬 탈출 2

import copy
import sys
input = sys.stdin.readline


def find_redball(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return True
    return False

def find_blueball(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                return True
    return False

def metrix_red(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return (i, j)

def metrix_blue(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                return (i, j)

def get_col(graph, y):
    tmp = []
    for i in range(N):
        tmp.append(graph[i][y])
    return tmp

def set_col(graph, y, arr):
    for i in range(N):
        graph[i][y] = arr[i]


def sort_array(arr):
    res, tmp = [], []
    for n in arr:
        if n == 0:
            tmp.append(n)
        elif n == -1 or n == 9:
            for t in tmp:
                res.append(t)
            tmp = []
            res.append(n)
        elif n == 1 or n == 2:
            if res[-1] == 9:
                tmp.append(0)
            else:
                res.append(n)
    return res


def move_left(graph):
    for i in range(N):
        graph[i] = sort_array(graph[i])
    return graph

def move_right(graph):
    for i in range(N):
        tmp = graph[i]
        tmp = sort_array(tmp[::-1])
        graph[i] = tmp[::-1]
    return graph

def move_upper(graph):
    for j in range(M):
        set_col(graph, j, sort_array(get_col(graph, j)))
    return graph

def move_down(graph):
    for j in range(M):
        tmp = get_col(graph, j)
        tmp = sort_array(tmp[::-1])
        set_col(graph, j, tmp[::-1])
    return graph

def init_graph():
    nums = {'#':-1, '.':0, 'R':1, 'B':2, 'O':9}
    for i in range(N):
        for j in range(M):
            graph[i][j] = nums[fst_graph[i][j]]

    
    
def bt(depth, graph, log):
    global MIN
    if depth > MIN:
        return
    if find_blueball(graph) and not find_redball(graph):
        MIN = min(MIN, depth)
        return
    if not find_blueball(graph):
        return
    
    gems = tuple(metrix_red(graph) + metrix_blue(graph))
    if gems in log:
        return
    log.add(gems)
    
    
    new_log = copy.deepcopy(log)
    new_graph = copy.deepcopy(graph)
    bt(depth+1, move_upper(new_graph), new_log)
    
    new_log = copy.deepcopy(log)
    new_graph = copy.deepcopy(graph)
    bt(depth+1, move_down(new_graph), new_log)
    
    new_log = copy.deepcopy(log)
    new_graph = copy.deepcopy(graph)
    bt(depth+1, move_left(new_graph), new_log)
    
    new_log = copy.deepcopy(log)
    new_graph = copy.deepcopy(graph)
    bt(depth+1, move_right(new_graph), new_log)
    
    return


N, M = map(int, input().split())
fst_graph = [[*map(str, input().strip())] for _ in range(N)]
graph = [[0] * M for _ in range(N)]
log = set()
MIN = 11
init_graph()

bt(0, graph, log)
if MIN == 11:
    print(-1)
else:
    print(MIN)
