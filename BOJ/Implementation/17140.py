# Solved on 2022. 2. 3.
# 17140 이차원 배열과 연산

from collections import defaultdict
import sys
input = sys.stdin.readline


def check_k():
    if len(A) < r or len(A[0]) < c:
        return False
    return A[r-1][c-1] == k

def change_row_col(graph):
    row, col = len(graph), len(graph[0])
    new_arr = [[graph[i][j] for i in range(row)] for j in range(col)]
    return new_arr

def cal_arr(graph):
    max_len = 0
    tmp, res = [], []
    for arr in graph:
        sorted_arr = sort_arr(arr)
        max_len = max(max_len, len(sorted_arr))
        tmp.append(sorted_arr)
    for arr in tmp:
        for _ in range(max_len-len(arr)):
            arr.append(0)
        res.append(arr)
    return res

def sort_arr(arr):
    dic = defaultdict(int)
    for n in arr:
        dic[n] += 1
    tmp = []
    for key in list(dic.keys()):
        if key == 0:
            continue
        tmp.append((key, dic[key]))
    tmp.sort(key=lambda x: (x[1], x[0]))
    tmp2 = []
    for a, b in tmp:
        tmp2.append(a)
        tmp2.append(b)
    return tmp2


r, c, k = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(3)]
time = 0
while time <= 100:
    if check_k():
        break
    
    time += 1
    if len(A) >= len(A[0]):
        A = cal_arr(A)
    else:
        A = change_row_col(cal_arr(change_row_col(A)))    

if time > 100:
    print(-1)
else:
    print(time)
