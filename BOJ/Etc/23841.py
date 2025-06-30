n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]

res = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m // 2):
        l = g[i][j]
        r = g[i][m - 1 - j]
        if l != '.':
            res[i][j] = l
        if r != '.':
            res[i][m - 1 - j] = r
        if l != '.' or r != '.':
            if l != '.':
                res[i][m - 1 - j] = l
            if r != '.':
                res[i][j] = r

for row in res:
    print(''.join(row))
