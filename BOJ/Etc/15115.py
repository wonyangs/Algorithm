import math

k, p, x = map(int, input().split())
v = math.sqrt(k * p / x)
print(f"{min(x * i + k * p / i for i in range(int(v), int(v) + 2) if i > 0):.3f}")
