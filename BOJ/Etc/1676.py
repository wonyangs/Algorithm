def count(N):
    t, f = 0, 0
    while N % 2 == 0:
        N //= 2
        t += 1
    while N % 5 == 0:
        N //= 5
        f += 1
    return (t, f)

N = int(input())

t, f = 0, 0
for i in range(1, N+1):
    a, b = count(i)
    t += a
    f += b
print(min(t, f))
