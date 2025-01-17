N, A, B = map(int, input().split())
p = b = 1
for _ in range(N):
    p, b = p + A, b + B
    if p < b: p, b = b, p
    elif p == b: b -= 1
print(p, b)
