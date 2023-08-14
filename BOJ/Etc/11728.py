N, M = map(int, input().split())
arr = [*map(int, input().split())] + [*map(int, input().split())]
arr.sort()
print(*arr)
