a, b, c = map(int, input().split())
print(sorted([a, b, c, a * b, a * c, b * c, a * b * c], key=lambda x: [x % 2, x])[-1])
