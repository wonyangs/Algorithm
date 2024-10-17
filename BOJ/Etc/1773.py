n, c = map(int, input().split())
print(len({t for p in [int(input()) for _ in range(n)] for t in range(p, c+1, p)}))
