def sigma(N):
    return N * (N + 1) // 2

a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(sigma(b) - sigma(a-1))
