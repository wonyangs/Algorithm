a, b = map(int, input().split()), map(int, input().split())
r = sum((x > y) - (x < y) for x, y in zip(a, b))
print("A" if r > 0 else "B" if r < 0 else "D")
