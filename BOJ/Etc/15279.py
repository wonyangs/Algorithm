n = int(input())
for _ in range(n):
    b, p = input().split()
    b = int(b)
    p = float(p)
    print(60 * (b - 1) / p, 60 * b / p, 60 * (b + 1) / p)
