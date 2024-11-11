A, B = map(int, input().split())
print(sum([i for i in range(1, 1001) for _ in range(i)][A-1:B]))
