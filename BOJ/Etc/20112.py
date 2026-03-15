n = int(input())
g = [input() for _ in range(n)]
print("YES" if all(g[i][j] == g[j][i] for i in range(n) for j in range(n)) else "NO")
