MIN = 1e9
for _ in range(int(input())):
    a, b = map(int, input().split())
    MIN = min(MIN, a + b)
print(MIN)
