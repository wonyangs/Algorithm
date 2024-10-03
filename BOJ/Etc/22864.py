A, B, C, M = map(int, input().split())
f = w = 0
for _ in range(24):
    if f + A <= M:
        f += A
        w += B
    else:
        f = max(0, f - C)
print(w)
