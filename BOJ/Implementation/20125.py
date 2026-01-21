import sys

input = sys.stdin.readline

N = int(input())
arr = [[*input().strip()] for _ in range(N)]

head_coor = None
for i in range(N):
    for j in range(N):
        if arr[i][j] == '*':
            head_coor = (i, j)
            break
    if head_coor:
        break

hx, hy = (head_coor[0] + 1, head_coor[1])

print(hx + 1, hy + 1)

res = []
def count(x, y, dx, dy):
    count = 0
    while 0 <= x < N and 0 <= y < N:
        if arr[x][y] == '*':
            count += 1
        x, y = x + dx, y + dy
    return count

res.append(count(hx, hy, 0, -1) - 1)
res.append(count(hx, hy, 0, 1) - 1)

body = count(hx, hy, 1, 0) - 1
res.append(body)

res.append(count(hx + body + 1, hy - 1, 1, 0))
res.append(count(hx + body + 1, hy + 1, 1, 0))

print(' '.join([str(i) for i in res]))
