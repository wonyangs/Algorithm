from itertools import combinations
N, M = map(int, input().split())
for com in combinations(sorted([*map(int, input().split())]), M): print(*com)
