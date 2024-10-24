a, b, n = 1, 1, int(input())
for _ in range(n-2): a, b = b, a + b
print(b if n > 1 else a)
