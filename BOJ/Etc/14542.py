c = 0
while True:
    n = int(input())
    if n == 0:
        break
    c += 1
    t = [list(map(int, input().split())) for _ in range(n)]
    s = sum(t[i][0] for i in range(n)) + sum(t[n-1][1:]) + sum(t[i][i] for i in range(1, n-1))
    print(f"Case #{c}:{s}")
