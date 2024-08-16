n, m = map(int, input().split())
castle = [input() for _ in range(n)]

rows = sum(1 for i in range(n) if 'X' not in castle[i])
cols = sum(1 for j in range(m) if 'X' not in [castle[i][j] for i in range(n)])

print(max(rows, cols))
