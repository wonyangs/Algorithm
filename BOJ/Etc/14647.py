n, m = map(int, input().split())
grid = [input().split() for _ in range(n)]
row = [sum(x.count('9') for x in grid[i]) for i in range(n)]
col = [sum(grid[i][j].count('9') for i in range(n)) for j in range(m)]
print(sum(row) - max(max(row), max(col)))
