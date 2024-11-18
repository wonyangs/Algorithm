m, n = map(int, input().split())
r, c, d, t = 0, 0, 0, 0
v = [[0] * n for _ in range(m)]
for _ in range(m * n - 1):
    v[r][c] = 1
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    nr, nc = r + dr[d], c + dc[d]
    if not (0 <= nr < m and 0 <= nc < n and not v[nr][nc]): d, t = (d + 1) % 4, t + 1
    r, c = r + dr[d], c + dc[d]
print(t)
