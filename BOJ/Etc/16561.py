n = int(input())
print(sum(1 for x in range(1, n // 3) for y in range(1, n // 3 - x) if n // 3 - x - y > 0))
