N, L, D = map(int, input().split())
t = 0
while any(i * (L + 5) <= t < i * (L + 5) + L for i in range(N)):
    t += D
print(t)
