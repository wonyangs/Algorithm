a, b = map(int, input().split())
print(1 if a - a * b * 0.01 < 100 else 0)
