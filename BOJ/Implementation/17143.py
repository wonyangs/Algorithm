# Solved on 2022. 2. 2.
# 17143 낚시왕

from collections import defaultdict
import sys
input = sys.stdin.readline


def shark_move(n, d, speed):
    if d == 1 or d == 2:
        speed %= 2*R - 2
    else:
        speed %= 2*C - 2

    if d == 1 and n == 1:
        d = 2
    elif d == 2 and n == R:
        d = 1
    elif d == 3 and n == C:
        d = 4
    elif d == 4 and n == 1:
        d = 3

    for _ in range(speed):
        if d == 1:
            n -= 1
            if n <= 1:
                d = 2
        elif d == 2:
            n += 1
            if n >= R:
                d = 1
        elif d == 3:
            n += 1
            if n >= C:
                d = 4
        elif d == 4:
            n -= 1
            if n <= 1:
                d = 3
    return (n, d)

R, C, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[(r, c)].append((s, d, z))

king_idx = 0
total_shark = 0
while king_idx < C:
    # 낚시왕이 오른쪽으로 한 칸 이동한다.
    king_idx += 1
    
    # 땅과 제일 가까운 상어를 잡는다.
    for i in range(1, R+1):
        if len(graph[(i, king_idx)]):
            total_shark += graph[(i, king_idx)][0][2]
            del(graph[(i, king_idx)])
            break
    
    # 상어가 이동한다.
    move = []
    for r, c in list(graph.keys()):
        if not len(graph[(r, c)]):
            continue
        speed, drc, size = graph[(r, c)][0]
        if drc == 1 or drc == 2:
            nr, d = shark_move(r, drc, speed)
            nc = c
        elif drc == 3 or drc == 4:
            nc, d = shark_move(c, drc, speed)
            nr = r
        move.append((nr, nc, speed, d, size))
    graph = defaultdict(list)
    for r, c, s, d, z in move:
        graph[(r, c)].append((s, d, z))
    for r, c in list(graph.keys()):
        graph[(r, c)].sort(key=lambda x: -x[2])
        graph[(r, c)] = graph[(r, c)][:1]
print(total_shark)
